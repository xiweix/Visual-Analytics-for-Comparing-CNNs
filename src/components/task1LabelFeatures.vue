<template>
  <v-container fluid>
    <!-- <v-card class="scrool" max-height="665"> -->
    <!-- <v-card class="scrool" max-height="700"> -->
    <v-card class="scrool" max-height="1035">
    <!-- <v-card class="scrool" max-height="1200"> -->
      <v-container fluid>
        <v-row v-if="$store.state.task1curImg!==null">
          <v-col>
            <div class="font-weight-medium">Original Image<br /></div>
            <div style="width:200px; height: 200px"><v-img :src="$store.state.task1curImg" width="200px" height="200px" contain></v-img></div>
          </v-col>
        </v-row>
        <v-row v-if="$store.state.task1curSimM!==null">
          <v-col>
            <div class="font-weight-medium">Similarity Matrix</div>
            <v-img :src="$store.state.task1curSimM" width="200" height="200" contain></v-img>
          </v-col>
        </v-row>
        <v-row v-for="(curName, index) in $store.state.task1imgSelection" :key="index">
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
import supBarChart1 from '@/components/supBarChart1.vue'
import supBarChart2 from '@/components/supBarChart2.vue'
import scatterData from '@/data/scatterData.js'

export default {
  name: 'task1LabelFeatures',

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
