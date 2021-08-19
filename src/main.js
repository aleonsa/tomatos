import { createApp } from 'vue'
import App from './App.vue'
import router from './router/index'
import firebase from 'firebase'

let app = null

firebase.auth().onAuthStateChanged(()=>{
    if (!app) {
        app = createApp(App).use(router).mount('#app')
    }
})






