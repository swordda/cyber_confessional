const { createApp } = Vue
createApp({
    el: ".app",
    data() {
        return {
            num: 0,
        }
    },
    methods: {
        yuClick() {
            console.log("yu");
            this.num += 1;
            if (this.num > 1000) {
                alert("佛祖：我超我怎么榜二了")
            }
        }

    }
}).mount('.app')