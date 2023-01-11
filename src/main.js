import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import vuetify from './plugins/vuetify'
import vueResource from 'vue-resource'
import websocket from 'vue-native-websocket'

Vue.config.productionTip = false
Vue.use(vueResource)
// Vue.use(websocket, 'ws://localhost:5050', {
// Vue.use(websocket, 'ws://192.168.1.86:5050', {
Vue.use(websocket, 'ws://169.237.4.185:5050', {

  reconnection: true,
  reconnectionAttempts: 5,
  reconnectionDelay: 3000
})

new Vue({
  router,
  store,
  vuetify,
  render: h => h(App)
}).$mount('#app')
