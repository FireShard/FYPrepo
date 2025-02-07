<template>
    <body style="background: url(&quot;assets/img/Aboutme.jpg&quot;) center / cover;">
        <div class="text-center mb-0 pb-0 mt-0 pt-5" style="padding-top: 150px;">
        <h1 class="mb-5">Enter Your Laptop Information</h1>
        
        <form class="pe-3 ms-0 ps-3" @submit.prevent="predictRamType">
            <div class="row" style="background: rgba(230,230,230,0.3);">
                <div class="col-xl-1"></div>
                <div class="col">
                    <label class="form-label" style="font-family: ABeeZee, sans-serif;">Manufacturer</label>
                    <input class="form-control" type="text" style="color: rgb(111,121,130);" placeholder="Lenovo" v-model="manufacturer">
                </div>
                <div class="col">
                    <label class="form-label" style="font-family: ABeeZee, sans-serif;">CPU Brand (Intel,AMD)</label>
                    <select class="form-select" v-model="CPUbrand">
                        <option value="Intel" selected="">Intel</option>
                        <option value="AMD">AMD</option>
                    </select>
                </div>
                <div class="col-xl-1"></div>
            </div>
            <div class="row" style="background: rgba(230,230,230,0.3);">
                <div class="col-xl-1"></div>
                <div class="col-xl-5">
                    <label class="form-label" style="font-family: ABeeZee, sans-serif;">Current RAM Size (GB)</label>
                    <input class="form-control" type="text" style="color: rgb(111,121,130);" placeholder="8" v-model="ramSize">
                </div>
                <div class="col">
                    <label class="form-label" style="font-family: ABeeZee, sans-serif;">CPU Name</label>
                    <input class="form-control" type="text" style="color: rgb(111,121,130);" placeholder="Core i5 / Ryzen 5" v-model="CPUName">
                </div>
                <div class="col-xl-1"></div>
            </div>
            <div class="row" style="background: rgba(230,230,230,0.3);">
                <div class="col-xl-1"></div>
                <div class="col"><label class="form-label" style="font-family: ABeeZee, sans-serif;">System Architecture</label>
                    <select class="form-select" v-model="architecture">
                        <option value="32-bit">32-bit</option>
                        <option value="64-bit" selected="">64-bit</option>
                    </select>
                </div>
                <div class="col">
                    <label class="form-label" style="font-family: ABeeZee, sans-serif;">CPU Generation</label>
                    <input class="form-control" type="text" style="color: rgb(111,121,130);" placeholder="7th, 8th, 9th, etc" v-model="CPUGen">
                </div>
                <div class="col-xl-1"></div>
            </div><button class="btn btn-primary btn-lg mt-2 me-3" type="submit">Submit</button>
        </form>
    </div>
</body>
</template>

<script>
import axios from "axios";

export default{
        name: "LaptopInfo",
        data(){
            return{
                manufacturer: "",
                ramSize: "",
                architecture: "",
                CPUbrand: "",
                CPUName: "",
                CPUGen: "",
                ramType: "",
                ramid: "1"
            }
        },

        methods: {
            addUserLaptop(){
                const newUserLaptop = {
                    manufacturer: this.manufacturer,
                    ramSize: this.ramSize,
                    architecture: this.architecture,
                    CPUbrand: this.CPUbrand,
                    CPUName: this.CPUName,
                    CPUGen: this.CPUGen,
                    ramType: this.ramType,
                    ramid: this.ramid
                };

                axios
                    .post("http://127.0.0.1:8000/UserLaptop/", newUserLaptop)
                    .then(response => {
                        console.log("Added Laptop Details Successfully", response.data);
                        alert("Added Laptop Details Successfully!");
                        this.goToRecommend();
                    })
                    .catch((error) =>{
                        console.error("Error in saving laptop data", error);
                        alert("Failed in saving laptop data. Please try again");
                    })     
            },
            goToRecommend(){
                this.$router.push({ 
                    path: '/recommend', 
                    query: { 
                    manufacturer: this.manufacturer, 
                    ramSize: this.ramSize, 
                    architecture: this.architecture, 
                    CPUbrand: this.CPUbrand, 
                    CPUName: this.CPUName, 
                    CPUGen: this.CPUGen, 
                    ramType: this.ramType 
                    } 
                });
            },

            async predictRamType() {
                try {

                    const response = await axios.post('http://127.0.0.1:8000/predictRAMType/',{
                        processor_brand: this.CPUbrand,
                        processor_name: this.CPUName,
                        processor_gnrtn: this.CPUGen,
                        os_bit: this.architecture,
                        brand: this.manufacturer,
                        ram_gb: this.ramSize,
                    });

                    console.log('Received data:', response.data);
                    this.ramType = response.data;
                    this.error = null;
                    console.log("RAM Type Predicted Successfully", response.data);
                    alert("RAM Type Predicted Successfully!");
                    this.goToRecommend();
                } 
                catch (error) {
                    console.error('Error predicting RAM type:', error);
                    this.ramType = 'Prediction Failed';
                    alert("Failed in predicting RAM type. Please try again");
                }
            },
        },
}
</script>