<template>
  <v-container fluid>
    <v-card-title>
      <v-row>
        <v-col cols="3">
          <v-text-field v-model="$store.state.task1search" append-icon="fas fa-search" label="Search" color="rgba(18,38,57,1)" single-line hide-details dense></v-text-field>
        </v-col>
        <v-spacer></v-spacer>
        <v-col cols="1">
          Threshold:
        </v-col>
        <v-col cols="3">
          <p> </p>
          <v-slider
            v-if="$store.state.task1TableReceive==true"
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
        <v-col cols="1">
          <v-icon small @click="exitExpPage">far fa-window-close</v-icon>
        </v-col>
      </v-row>
    </v-card-title>
    <!-- <v-row justify="end">
      <v-col md="1">
        <v-icon small @click="exitExpPage">far fa-window-close</v-icon>
      </v-col>
    </v-row> -->
    <v-row>
      <v-col>
        <task1ExpTable />
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import task1ExpTable from '@/components/task1ExpTable.vue'

export default {
  name: 'task1ExpResult',

  components: {
    task1ExpTable
  },

  data: () => ({
    threshold: 0.0
  }),

  methods: {
    initExpResult: function () {
      this.$store.state.task1curSimM = null
      this.$store.state.task1ExpRes = []
    },
    exitExpPage: function () {
      this.initExpResult()
      this.$store.state.task1OrgPage = true
      this.$store.state.task1curImg = null
    },
    updateTable (threshold) {
      this.$store.state.task1ExpRes = []
      this.$socket.send('requestTask1Update***' + threshold)
    }
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('InitTask1Exp***') !== -1) {
        this.initExpResult()
      } else if (res.indexOf('task1curSimM***') !== -1) {
        res = res.split('***')
        this.$store.state.task1curSimM = 'data:image/png;base64,' + res[1]
      }
    }
  }
}
</script>
