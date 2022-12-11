

const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data(){
        return{
            message: 'Is this working?',
        

        

        }
    },
    methods:{
        
        animateLogo() {
            gsap.to('#title-hi', {duration: 2, top: '2rem', left: '2rem', color: 'red'})
        }


        
        
    },
    mounted(){
        console.log('hello')
        this.animateLogo()
       
      
       
    },
})