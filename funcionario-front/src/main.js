import Vue from 'vue'
import './plugins/vuetify'
import App from './App.vue'
import router from './router'
import axios from 'axios'  
import VueAxios from 'vue-axios'

Vue.config.productionTip = false

axios.defaults.baseURL = 'http://api.fundrhi.pythonlab.com.br/api';
Vue.use(VueAxios, axios)

new Vue({
  render: h => h(App),
  router,
}).$mount('#app')
