<template>
  <v-container fluid>
    <v-card-text>Overall Accuracy</v-card-text>
    <barChart id="modelAcc" :dataset="accInfo" :rotate="true"></barChart>
  </v-container>
</template>

<script>
import barChart from '@/components/barChart'
import modelAccData from '@/data/modelAccData.js'

export default {
  name: 'modelAcc',

  components: {
    barChart
  },

  data: () => ({
    accInfo: modelAccData.modelAccInfo
  }),

  created: function () {
    // console.log(this.accInfo)
  }
}
</script>
