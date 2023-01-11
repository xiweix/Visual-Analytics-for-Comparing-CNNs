<template>
  <v-container fluid>
    <!-- <v-card class="scrool mx-auto" max-height="620"> -->
    <!-- <v-card class="scrool mx-auto" max-height="700"> -->
    <v-card class="scrool mx-auto" max-height="1035">
    <!-- <v-card class="scrool mx-auto" max-height="1200"> -->
      <v-container fluid>
        <v-row v-for="(curName, index) in $store.state.task2imgSelection" :key="index">
          <v-col>
            <labelScatterChart :id="curName" :dataPoint="labelInformation[curName]"/>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <supBarChart1 />
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            <supBarChart2 />
          </v-col>
        </v-row>
      </v-container>
    </v-card>
  </v-container>
</template>

<script>
import labelScatterChart from '@/components/labelScatterChart.vue'
import scatterData from '@/data/scatterData.js'
import supBarChart1 from '@/components/supBarChart1.vue'
import supBarChart2 from '@/components/supBarChart2.vue'

export default {
  name: 'task2LabelFeatures',

  components: {
    labelScatterChart,
    supBarChart1,
    supBarChart2
  },

  data: () => ({
    labelInformation: scatterData.labelInfo
  }),

  methods: {
    check: function () {
      console.log(this.labelInformation)
    }
  },

  watch: {
  }
}
</script>

<style>
.scrool {
  overflow-y: auto
}
</style>
