<template>
  <v-container fluid>
    <!-- <v-card class="scrool" max-height="665"> -->
    <!-- <v-card class="scrool" max-height="700"> -->
    <v-card class="scrool" max-height="1050">
      <v-row no-gutters>
        <v-col cols="1">
          <v-card-text>
            Example model:
          </v-card-text>
        </v-col>
        <v-col cols="2">
          <v-card-text>
            <v-select dense v-model="curModelLocal" :items="modelItems" color="rgba(18,38,57,1)"></v-select>
          </v-card-text>
        </v-col>
        <v-col cols="2">
          <v-card-text>
            <span v-if="expAcc!==null">Overall Accuracy: {{ expAcc }}%</span>
          </v-card-text>
        </v-col>
        <v-col cols="1">
          <v-card-text>
            Threshold:
          </v-card-text>
        </v-col>
        <v-col cols="4">
          <v-card-text>
            <p> </p>
            <v-slider
              v-if="receiveAll==true"
              @mouseup="updateTable(threshold)"
              dense
              v-model="threshold"
              :thumb-size="24"
              thumb-label="always"
              step="0.2"
              min="0.0"
              max="0.9"
            ></v-slider>
            <v-slider
              v-else
              readonly
              dense
              v-model="threshold"
              :thumb-size="24"
              thumb-label="always"
              step="0.2"
              min="0.0"
              max="0.9"
            ></v-slider>
          </v-card-text>
        </v-col>
      </v-row>
      <v-data-table :headers="headers" :items="expExamples" :loading="!receiveAll" multi-sort dense :items-per-page=3 class="elevation-1">
        <template v-slot:item.org="{ item }">
          <v-img :aspect-ratio="100/100" :src="item.org" max-height="250" width="250" contain></v-img>
        </template>
        <template v-slot:item.gcam="{ item }">
          <!-- <svg>{{ item.gcam }}</svg> -->
          <v-img :src="item.gcam" width="250" contain></v-img>
        </template>
        <template v-slot:item.bbmp="{ item }">
          <v-img :src="item.bbmp" width="250" contain></v-img>
        </template>
        <template v-slot:item.gcampp="{ item }">
          <v-img :src="item.gcampp" width="250" contain></v-img>
        </template>
        <template v-slot:item.sgcampp="{ item }">
          <v-img :src="item.sgcampp" width="250" contain></v-img>
        </template>
        <template v-slot:item.scam="{ item }">
          <v-img :src="item.scam" width="250" contain></v-img>
        </template>
      </v-data-table>
    </v-card>
  </v-container>
</template>

<script>
// import * as d3 from 'd3'
export default {
  name: 'exampleExp',

  props: {
    curModel: String
  },

  data: () => ({
    threshold: 0.0,
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
        align: 'center',
        sortable: false,
        value: 'org'
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
        align: 'center',
        sortable: false,
        value: 'gcam'
      },
      {
        text: 'BBMP',
        align: 'center',
        sortable: false,
        value: 'bbmp'
      },
      {
        text: 'Grad-CAM++',
        align: 'center',
        sortable: false,
        value: 'gcampp'
      },
      {
        text: 'Score-CAM',
        align: 'center',
        sortable: false,
        value: 'scam'
      },
      {
        text: 'Smooth Grad-CAM++',
        align: 'center',
        sortable: false,
        value: 'sgcampp'
      },
      {
        text: 'Ground Truth(Predicted)',
        align: 'center',
        sortable: true,
        value: 'label'
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
    },
    updateTable (threshold) {
      this.initPage()
      this.$socket.send('Ready***' + this.$store.state.viewModelIdx + '***' + threshold)
    }
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('mainPageExample***') !== -1) {
        res = res.split('***')
        this.threshold = parseFloat(res[9])
        // console.log(typeof res[4])
        // const gradCamMaskTemp = JSON.parse(res[4])
        // const width = 224
        // const height = 224
        // const thresholds = 5
        // const extent = d3.extent(gradCamMaskTemp)
        // const contours = d3.contours()
        //   .size([width, height])
        //   .thresholds(d3.range(extent[0], extent[1], (extent[1] - extent[0]) / thresholds))
        // const contoursData = contours(gradCamMaskTemp)
        // const projection = d3.geoIdentity()
        //   .fitSize([100, 100], contoursData[0])
        // const path = d3.geoPath()
        //   .projection(projection)
        // const svg = d3.select('body').append('svg')
        // const paths = svg.selectAll(null)
        //   .data(contoursData)
        //   .enter()
        //   .append('path')
        //   .attr('d', path)
        // const gradCamMask = []
        // while (gradCamMaskTemp.length) gradCamMask.push(gradCamMaskTemp.splice(0, 224))
        // const c = d3.contours(gradCamMask)
        // console.log(typeof gradCamMask, gradCamMask.length, gradCamMask[0].length)
        this.expExamples.push({
          org: 'data:image/png;base64,' + res[1],
          gcam: 'data:image/png;base64,' + res[4],
          bbmp: 'data:image/png;base64,' + res[5],
          gcampp: 'data:image/png;base64,' + res[6],
          scam: 'data:image/png;base64,' + res[8],
          sgcampp: 'data:image/png;base64,' + res[7],
          label: res[2] + '(' + res[3] + ')'
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
          this.$socket.send('Ready***' + this.$store.state.viewModelIdx + '***' + this.threshold)
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
