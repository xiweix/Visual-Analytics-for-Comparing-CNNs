import Vue from 'vue'
import Vuetify from 'vuetify/lib'
// import 'material-design-icons-iconfont/dist/material-design-icons.css'
import '@fortawesome/fontawesome-free/css/all.css'

Vue.use(Vuetify)

export default new Vuetify({
  icons: {
    // iconfont: 'md'
    iconfont: 'fa'
  }
})
