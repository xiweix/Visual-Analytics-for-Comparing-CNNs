<template>
  <v-container fluid>
    <v-data-table :headers="headers" :items="$store.state.task1ExpRes" :loading="!$store.state.task1TableReceive" :items-per-page="15" :search="$store.state.task1search" multi-sort dense class="elevation-1">
      <template v-slot:item.exp="{ item }">
        <v-img :src="item.exp" width="300" contain></v-img>
      </template>
      <template v-slot:item.expwithimg="{ item }">
        <v-img :src="item.expwithimg" width="300" contain></v-img>
      </template>
    </v-data-table>
  </v-container>
</template>

<script>
export default {
  name: 'task1ExpTable',

  data: () => ({
    headers: [
      {
        text: 'Model (Overall Accuracy)',
        align: 'center',
        sortable: true,
        value: 'model'
      },
      {
        text: 'Visual Explanation',
        align: 'center',
        sortable: false,
        value: 'exp'
      },
      {
        text: 'Explanation on Image',
        align: 'center',
        sortable: false,
        value: 'expwithimg'
      },
      {
        text: 'Ground Truth (Predicted)',
        align: 'center',
        sortable: true,
        value: 'rellabel'
      },
      {
        text: 'Class Accuracy',
        align: 'center',
        value: 'labelacc'
      },
      // {
      //   text: 'Predicted',
      //   sortable: true,
      //   value: 'prdlabel',
      //   width: '110'
      // },
      {
        text: 'Confidence Score',
        align: 'center',
        value: 'certainty'
      }
    ]
  }),

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('task1curTable***') !== -1) {
        this.$store.state.task1TableReceive = false
        res = res.split('***')
        this.$store.state.task1ExpRes.push({
          model: res[1] + ' (' + res[2] + ')',
          labelacc: res[3],
          rellabel: res[4] + ' (' + res[5] + ')',
          // prdlabel: res[5],
          certainty: res[6],
          exp: 'data:image/png;base64,' + res[7],
          expwithimg: 'data:image/png;base64,' + res[8]
        })
      } else if (res.indexOf('task1curTableFinish***') !== -1) {
        res = res.split('***')
        this.$store.state.task1TableReceive = true
        console.log('receive Task1 full table')
      }
    }
  }
}
</script>
