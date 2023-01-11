<template>
  <v-container fluid>
    <!-- <v-card class="scrool" max-height="620"> -->
    <!-- <v-card class="scrool" max-height="700"> -->
    <v-card class="scrool" max-height="1000">
    <!-- <v-card class="scrool" max-height="1200"> -->
      <v-card-title>
        <v-spacer></v-spacer>
        <v-btn text @click="exitTask2" color="rgba(18,38,57,1)">EXIT TASK</v-btn>
      </v-card-title>
      <v-card-title v-if="task2Model!==null && task2ModelAcc!==null">
        <v-row>
          <v-col cols="2">
            <v-text-field v-model="search" append-icon="fas fa-search" label="Search" color="rgba(18,38,57,1)" single-line hide-details dense></v-text-field>
          </v-col>
          <v-col cols="3">
            Model: {{ task2Model }}. Overall Accuracy: {{ task2ModelAcc }}%.
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="1">
            Threshold:
          </v-col>
          <v-col cols="2">
            <p> </p>
            <v-slider
              v-if="task2ExpDone==true"
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
          </v-col>
          <v-spacer></v-spacer>
          <v-col cols="2">
            <v-switch v-if="$store.state.task2modelSelection.indexOf('resnet152')!==-1 && $store.state.task2expSelection.indexOf('Smooth Grad-CAM++')!==-1" v-model="viewRGB" color="rgba(18,38,57,1)" dense label="Color Intensity Histogram"></v-switch>
          </v-col>
        </v-row>
      </v-card-title>
      <v-row>
        <v-col>
          <!-- <v-card class="scrool" max-height="580"> -->
          <v-card v-if="!viewRGB">
            <v-data-table :headers="headers" :items="task2ExpResult" :loading="!task2ExpDone" :search="search" multi-sort dense class="elevation-1">
              <template v-slot:item.org="{ item }">
                <v-img :aspect-ratio="100/100" :src="item.org" max-height="300" width="300" contain></v-img>
              </template>
              <template v-slot:item.exp="{ item }">
                <v-img :src="item.exp" width="300" contain></v-img>
              </template>
              <template v-slot:item.expwithimg="{ item }">
                <v-img :src="item.expwithimg" width="300" contain></v-img>
              </template>
            </v-data-table>
          </v-card>
          <v-card v-else>
            <v-data-table :headers="headers2" :items="task2ExpResult2" :loading="!task2ExpDone" :search="search" multi-sort dense class="elevation-1">
              <template v-slot:item.org="{ item }">
                <v-img :aspect-ratio="100/100" :src="item.org" max-height="300" width="300" contain></v-img>
              </template>
              <template v-slot:item.exp="{ item }">
                <v-img :src="item.exp" width="300" contain></v-img>
              </template>
              <template v-slot:item.expwithimg="{ item }">
                <v-img :src="item.expwithimg" width="300" contain></v-img>
              </template>
              <template v-slot:item.rgbHist="{ item }">
                <v-img :src="item.rgbHist" width="300" contain></v-img>
              </template>
            </v-data-table>
          </v-card>
        </v-col>
      </v-row>
    </v-card>
  </v-container>
</template>

<script>
export default {
  name: 'task2Main',

  data: () => ({
    threshold: 0.0,
    task2Model: null,
    task2ModelAcc: null,
    task2ExpDone: false,
    task2ExpResult: [],
    task2ExpResult2: [],
    viewRGB: false,
    search: '',
    headers: [
      {
        text: 'Original Image',
        align: 'center',
        sortable: false,
        // width: '120',
        value: 'org'
      },
      {
        text: 'Ground Truth (Predicted)',
        align: 'center',
        sortable: true,
        // width: '120',
        value: 'label'
      },
      {
        text: 'Class Accuracy',
        align: 'center',
        // width: '124',
        value: 'labelacc'
      },
      {
        text: 'Confidence Score',
        align: 'center',
        // width: '140',
        value: 'certainty'
      },
      {
        text: 'Visual Explanation',
        align: 'center',
        sortable: false,
        // width: '120',
        value: 'exp'
      },
      {
        text: 'Explanation on Image',
        align: 'center',
        sortable: false,
        // width: '150',
        value: 'expwithimg'
      }
    ],
    headers2: [
      {
        text: 'Original Image',
        align: 'center',
        sortable: false,
        // width: '12',
        value: 'org'
      },
      {
        text: 'Ground Truth (Predicted)',
        align: 'center',
        sortable: true,
        // width: '5',
        value: 'label'
      },
      {
        text: 'Class Accuracy',
        align: 'center',
        // width: '12',
        value: 'labelacc'
      },
      {
        text: 'Confidence Score',
        align: 'center',
        // width: '120',
        value: 'certainty'
      },
      {
        text: 'Visual Explanation',
        align: 'center',
        sortable: false,
        // width: '12',
        value: 'exp'
      },
      {
        text: 'Explanation on Image',
        align: 'center',
        sortable: false,
        // width: '12',
        value: 'expwithimg'
      },
      {
        text: 'ColorIntensityDistribution',
        align: 'center',
        sortable: false,
        // width: '12',
        value: 'rgbHist'
      }
    ]
  }),

  methods: {
    initTask2: function () {
      this.task2Model = null
      this.task2ModelAcc = null
      this.task2ExpDone = false
      this.task2ExpResult = []
      this.task2ExpResult2 = []
    },
    exitTask2: function () {
      this.$store.state.taskState = 0
      this.initTask2()
      // this.$socket.send('Ready')
      this.$socket.send('Ready***' + this.$store.state.viewModelIdx + '***' + '0.0')
    },
    updateTable (threshold) {
      this.$socket.send('runTask2***' + this.$store.state.task2modelSelection + '***' + this.$store.state.task2imgSelection + '***' + this.$store.state.task2expSelection + '***' + threshold)
    }
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('InitTask2***') !== -1) {
        this.initTask2()
        console.log('initialize task 2')
      } else if (res.indexOf('task2ImgResult***') !== -1) {
        this.task2ExpDone = false
        res = res.split('***')
        this.task2ExpResult.push({
          org: 'data:image/png;base64,' + res[1],
          label: res[2] + '(' + res[4] + ')',
          labelacc: res[3],
          certainty: res[5],
          exp: 'data:image/png;base64,' + res[6],
          expwithimg: 'data:image/png;base64,' + res[7]
        })
        this.task2ExpResult2.push({
          org: 'data:image/png;base64,' + res[1],
          label: res[2] + '(' + res[4] + ')',
          labelacc: res[3],
          certainty: res[5],
          exp: 'data:image/png;base64,' + res[6],
          expwithimg: 'data:image/png;base64,' + res[7],
          rgbHist: 'data:image/png;base64,' + res[8]
        })
      } else if (res.indexOf('task2ImgDone***') !== -1) {
        res = res.split('***')
        this.task2Model = res[1]
        this.task2ModelAcc = res[2]
        this.task2ExpDone = true
      }
    }
  }
}
</script>

<style>
.scrool {
  overflow-y: auto
}
.v-card__title {
  font-size: 15px;
  font-weight: 500;
  padding: 5px
  /* font-family: default */
}
.v-label {
  font-size: 15px;
  font-family: default
}
.v-icon.v-icon {
  font-size: 15px
}
</style>
