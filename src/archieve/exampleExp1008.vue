<template>
  <v-container fluid>
    <!-- <v-card class="scrool" max-height="665"> -->
    <!-- <v-card class="scrool" max-height="700"> -->
    <v-card class="scrool" max-height="1100">
      <v-card-text>
        Example model:
        <v-select dense v-model="curModelLocal" :items="modelItems" color="rgba(18,38,57,1)"></v-select>
        <span v-if="expAcc!==null">Overall Accuracy: {{ expAcc }}%</span>
      </v-card-text>
      <v-data-table :headers="headers" :items="expExamples" :loading="!receiveAll" multi-sort dense :items-per-page=9 class="elevation-1">
        <template v-slot:item.org="{ item }">
          <v-img :aspect-ratio="100/100" :src="item.org" contain></v-img>
        </template>
        <template v-slot:item.gcam="{ item }">
          <svg>{{ item.gcam }}</svg>
          <!-- <v-img :src="item.gcam" width="100" contain></v-img> -->
        </template>
        <template v-slot:item.bbmp="{ item }">
          <v-img :src="item.bbmp" width="100" contain></v-img>
        </template>
        <template v-slot:item.gcampp="{ item }">
          <v-img :src="item.gcampp" width="100" contain></v-img>
        </template>
        <template v-slot:item.sgcampp="{ item }">
          <v-img :src="item.sgcampp" width="100" contain></v-img>
        </template>
        <template v-slot:item.scam="{ item }">
          <v-img :src="item.scam" width="100" contain></v-img>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
import * as d3 from 'd3'
export default {
  name: 'exampleExp',

  props: {
    curModel: String
  },

  data: () => ({
    curModelLocal: null,
    receiveAll: false,
    expExamples: [],
    expAcc: null,
    modelItems: [
      'mobilenet_v2',
      'alexnet',
      'resnet18',
      'resnet34',
      'resnet50',
      'resnet101',
      'resnet152',
      'densenet121',
      'densenet161',
      'densenet169',
      'densenet201',
      'squeezenet1_1',
      'shufflenet_v2_x0_5'
    ],
    headers: [
      {
        text: 'Original Image',
        align: 'start',
        sortable: false,
        value: 'org'
      },
      {
        text: 'Ground Truth(Predicted)',
        sortable: true,
        value: 'label'
      },
      // {
      //   text: 'Label Accuracy',
      //   value: 'lableacc'
      // },
      // {
      //   text: 'Predicted',
      //   sortable: true,
      //   value: 'prdlabel'
      // },
      // {
      //   text: 'Certainty',
      //   value: 'certainty'
      // },
      {
        text: 'Grad-CAM',
        sortable: false,
        value: 'gcam'
      },
      {
        text: 'BBMP',
        sortable: false,
        value: 'bbmp'
      },
      {
        text: 'Grad-CAM++',
        sortable: false,
        value: 'gcampp'
      },
      {
        text: 'Smooth Grad-CAM++',
        sortable: false,
        value: 'sgcampp'
      },
      {
        text: 'Score-CAM',
        sortable: false,
        value: 'scam'
      }
    ]
  }),

  methods: {
    mapModel (modelName) {
      const m = new Map()
      m.set('mobilenet_v2', 0)
      m.set('alexnet', 1)
      m.set('resnet18', 2)
      m.set('resnet34', 3)
      m.set('resnet50', 4)
      m.set('resnet101', 5)
      m.set('resnet152', 6)
      m.set('densenet121', 7)
      m.set('densenet161', 8)
      m.set('densenet169', 9)
      m.set('densenet201', 10)
      m.set('squeezenet1_1', 11)
      m.set('shufflenet_v2_x0_5', 12)
      return m.get(modelName)
    },
    initPage () {
      this.receiveAll = false
      this.expExamples = []
      this.expAcc = null
    }
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('mainPageExample***') !== -1) {
        res = res.split('***')
        console.log(typeof res[4])
        const gradCamMaskTemp = JSON.parse(res[4])
        const width = 224
        const height = 224
        const thresholds = 5
        const extent = d3.extent(gradCamMaskTemp)
        const contours = d3.contours()
          .size([width, height])
          .thresholds(d3.range(extent[0], extent[1], (extent[1] - extent[0]) / thresholds))
        const contoursData = contours(gradCamMaskTemp)
        const projection = d3.geoIdentity()
          .fitSize([100, 100], contoursData[0])
        const path = d3.geoPath()
          .projection(projection)
        const svg = d3.select('body').append('svg')
        const paths = svg.selectAll(null)
          .data(contoursData)
          .enter()
          .append('path')
          .attr('d', path)
        const gradCamMask = []
        while (gradCamMaskTemp.length) gradCamMask.push(gradCamMaskTemp.splice(0, 224))
        // const c = d3.contours(gradCamMask)
        // console.log(typeof gradCamMask, gradCamMask.length, gradCamMask[0].length)
        this.expExamples.push({
          org: 'data:image/png;base64,' + res[1],
          label: res[2] + '(' + res[3] + ')',
          gcam: paths,
          bbmp: 'data:image/png;base64,' + res[5],
          gcampp: 'data:image/png;base64,' + res[6],
          sgcampp: 'data:image/png;base64,' + res[7],
          scam: 'data:image/png;base64,' + res[8]
          // org: 'data:image/png;base64,' + res[1],
          // label: res[2],
          // lableacc: res[3],
          // prdlabel: res[4],
          // certainty: res[5],
          // gcam: 'data:image/png;base64,' + res[6],
          // bbmp: 'data:image/png;base64,' + res[7],
          // gcampp: 'data:image/png;base64,' + res[8],
          // sgcampp: 'data:image/png;base64,' + res[9],
          // scam: 'data:image/png;base64,' + res[10]
        })
      } else if (res.indexOf('FinishMainPageExample***') !== -1) {
        res = res.split('***')
        this.expAcc = res[1]
        this.receiveAll = true
        console.log('Receive visual explanation examples of model "' + this.curModelLocal + '"')
      }
    }
  },

  created: function () {
    this.curModelLocal = this.curModel
  },

  watch: {
    curModelLocal: {
      handler (newVal, oldVal) {
        this.initPage()
        if (oldVal !== null) {
          if (newVal !== this.$store.state.viewModel) {
            this.$store.state.viewModel = newVal
            this.$store.state.viewModelIdx = this.mapModel(newVal)
          }
          this.$socket.send('Ready***' + this.$store.state.viewModelIdx)
        }
      }
    },
    curModel: {
      handler (newVal, oldVal) {
        this.initPage()
        this.curModelLocal = newVal
      }
    }
  }
}
</script>

<style>
.scrool {
  overflow-y: auto
}
</style>
