<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="auto">
        <scatterChart id='overall'/>
      </v-col>
      <v-col cols="auto">
        <radarChart />
      </v-col>
      <v-col cols="auto">
        <barModelChart :modelIdx="$store.state.viewModelIdx" :modelName="$store.state.viewModel"/>
      </v-col>
      <v-col cols="auto">
        <barLabelChart :modelIdx="$store.state.viewModelIdx" :modelName="$store.state.viewModel" :parentIdx="$store.state.viewLabelIdx" :parentName="$store.state.viewLabel"/>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import scatterChart from '@/components/scatterChart.vue'
import radarChart from '@/components/radarChart.vue'
import barModelChart from '@/components/barModelChart.vue'
import barLabelChart from '@/components/barLabelChart.vue'

export default {
  name: 'OverallFeatures',

  components: {
    scatterChart,
    radarChart,
    barModelChart,
    barLabelChart
  },

  data: () => ({
  }),

  methods: {
  },

  watch: {
  }
}
</script>
