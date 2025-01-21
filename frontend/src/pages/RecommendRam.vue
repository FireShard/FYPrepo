<template>
    <body style="background: url(&quot;assets/img/Aboutmev2.jpg&quot;);background-size: cover;">
    <div class="text-center pb-0 mb-5">
        <h1 class="mt-5">Your Compatible RAM Type:&nbsp;</h1>
        <h1 style="color: #5bdc3b;font-size: 50px;background: rgba(241,241,241,0.35);">DDR4</h1>
    </div>
    <p style="text-align: center;">Here are compatible RAMs that you can buy from Shopee:</p>
    <div>
        <div class="table-responsive">
            <table class="table">
                <thead>
                    <tr>
                        <th>RAM Brand</th>
                        <th>Shopee Link</th>
                    </tr>
                </thead>
                <tbody>
                    <tr>
                        <td>Cell 1</td>
                        <td>Cell 2</td>
                    </tr>
                    <tr>
                        <td>Cell 3</td>
                        <td>Cell 4</td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</body>
</template>

<script>
    import axios from "axios";

    export default{
        name: "Recommend",
        UserLapData(){
            return{
                userLaptop:{
                    manufacturer: "",
                    ramSize: "",
                    architecture: "",
                    CPUbrand: "",
                    CPUName: "",
                    CPUGen: "",
                    ramType: "",
                }
            }
        },

        mounted(){
            this.fetchUserLaptop();
        },

        methods:{
            async fetchUserLaptop() {
                try {
                    const response = await axios.get("http://127.0.0.1:8000/UserLaptop");

                    // Log success to the console
                    console.log("User Laptop Data fetched successfully:", response.data);

                    // Assuming 'UserLapData' is the correct field from the response
                    this.userLaptop = response.data.UserLapData;

                } catch (err) {
                    // Log error message to the console
                    this.error = "Failed to fetch User Laptop Data";
                    console.error("Error fetching data:", err);
                }
            }
        }
    }
</script>