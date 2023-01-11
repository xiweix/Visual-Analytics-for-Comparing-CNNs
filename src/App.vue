<template>
  <v-app id="App">
    <!-- <v-app-bar app color="rgba(27,36,49,1)" dense flat dark> -->
    <v-app-bar app color="rgba(18,38,57,1)" dense flat dark>
      <v-toolbar-title class="font-weight-bold subtitle-1">
        Visual Analytics System for Comparative Study of Deep Convolutional Neural Networks
      </v-toolbar-title>
    </v-app-bar>
    <v-content>
      <mainPage />
    </v-content>
  </v-app>
</template>

<script lang="ts">
import Vue from 'vue'
import mainPage from './views/mainPage.vue'

export default Vue.extend({
  name: 'App',

  components: {
    mainPage
  },

  data: () => ({
  })
})
</script>
