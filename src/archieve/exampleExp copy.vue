<template>
  <v-container fluid>
    <v-card class="scrool" max-height="700">
      <v-card-text v-if="expModel!==null">Example model: {{ expModel }}. Overall Accuracy: {{ expAcc }}%</v-card-text>
      <v-data-table :headers="headers" :items="expExamples" :loading="!receiveAll" multi-sort dense class="elevation-1">
        <template v-slot:item.org="{ item }">
          <v-img :src="item.org" width="100" contain></v-img>
        </template>
        <template v-slot:item.gcam="{ item }">
          <v-img :src="item.gcam" width="100" contain></v-img>
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
export default {
  name: 'exampleExp',

  data: () => ({
    receiveAll: false,
    expExamples: [],
    expModel: null,
    expAcc: null,
    windowHeight: 700,
    headers: [
      {
        text: 'OrgImg',
        align: 'start',
        sortable: false,
        value: 'org'
      },
      {
        text: 'Label',
        sortable: false,
        value: 'label'
      },
      // {
      //   text: 'Label Accuracy',
      //   value: 'lableacc'
      // },
      {
        text: 'Predict Label',
        sortable: false,
        value: 'prdlabel'
      },
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
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('mainPageExample***') !== -1) {
        res = res.split('***')
        this.expExamples.push({
          org: 'data:image/png;base64,' + res[1],
          label: res[2],
          prdlabel: res[3],
          gcam: 'data:image/png;base64,' + res[4],
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
        this.expModel = res[1]
        this.expAcc = res[2]
        this.receiveAll = true
        console.log('receive full table')
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
