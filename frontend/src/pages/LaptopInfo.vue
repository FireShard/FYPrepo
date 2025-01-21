<template>
    <body style="background: url(&quot;assets/img/Aboutme.jpg&quot;) center / cover;">
        <div class="text-center mb-0 pb-0 mt-0 pt-5" style="padding-top: 150px;">
        <h1 class="mb-5">Enter Your Laptop Information</h1>
        
        <form class="pe-3 ms-0 ps-3" @submit.prevent="addUserLaptop">
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
            </div><button class="btn btn-primary btn-lg mt-2 me-3" type="submit" @click="goToRecommend">Submit</button>
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
            }
        },

        methods: {
            addUserLaptop(){
                const newUserLaptop = {
                    manufacturer: this.manufacturer,
                    ramSize: this.ramSize,
                    architecture: this.architecture,
                    CPUbrand: this.architecture,
                    CPUName: this.architecture,
                    CPUGen: this.architecture,
                    ramType: this.architecture,
                };

                axios
                    .post("http://127.0.0.1:8000/UserLaptop", newUserLaptop)
                    .then(response => {
                        console.log("Added Laptop Details Successfully", response.data);
                        alert("Added Laptop Details Successfully!");
                    })
                    .catch((error) =>{
                        console.error("Error in saving laptop data", error)
                        alert("Failed in saving laptop data. Please try again");
                    })     
            },
            goToRecommend(){
                this.$router.push("/recommend");
            },
        },
    };
</script>