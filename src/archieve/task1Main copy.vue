<template>
  <v-container fluid>
    <v-card>
      <v-row justify="end">
        <v-col v-if="task1OrgDone" cols="10">
          <v-card-text>The Label is <strong>"{{ task1Label }}"</strong>. Click the image to view the comparison results.</v-card-text>
        </v-col>
        <v-col cols="2">
          <v-btn text @click="exitTask1" color="rgba(18,38,57,1)">EXIT TASK</v-btn>
        </v-col>
      </v-row>
      <v-card class="scrool" max-height="622">
        <v-row v-if="$store.state.task1OrgPage">
          <v-col v-for="orgImg in task1OrgImg" :key="orgImg.id">
            <v-img v-if="task1OrgDone" @click="requestTask1Exp(orgImg.id, orgImg.img)" :src="orgImg.img" height="150" width="150" contain>
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                </v-row>
              </template>
            </v-img>
            <v-img v-else :src="orgImg.img" height="150" width="150" contain>
              <template v-slot:placeholder>
                <v-row class="fill-height ma-0" align="center" justify="center">
                  <v-progress-circular indeterminate color="grey lighten-5"></v-progress-circular>
                </v-row>
              </template>
            </v-img>
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col>
            <task1ExpResult />
          </v-col>
        </v-row>
      </v-card>
    </v-card>
  </v-container>
</template>

<script>
import task1ExpResult from '@/components/task1ExpResult.vue'

export default {
  name: 'task1Main',

  components: {
    task1ExpResult
  },

  data: () => ({
    task1OrgImg: [],
    task1OrgDone: false,
    task1Label: null
  }),

  methods: {
    initTask1: function () {
      this.task1OrgImg = []
      this.task1OrgDone = false
      this.task1Label = null
      this.$store.state.task1OrgPage = true
      this.$store.state.task1curImg = null
      this.$store.state.task1curSimM = null
    },

    requestTask1Exp: function (res1, res2) {
      this.$store.state.task1OrgPage = false
      this.$store.state.task1curImg = res2
      this.$socket.send('requestTask1Exp***' + res1)
    },

    exitTask1: function () {
      this.$store.state.taskState = 0
      // this.$socket.send('Ready')
      this.$socket.send('Ready***' + this.$store.state.viewModelIdx)
      this.initTask1()
    }
  },

  mounted () {
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('InitTask1***') !== -1) {
        this.initTask1()
      } else if (res.indexOf('task1ImgResult***') !== -1) {
        res = res.split('***')
        this.task1OrgImg.push({ id: res[1], img: 'data:image/png;base64,' + res[2] })
      } else if (res.indexOf('task1ImgDone***') !== -1) {
        res = res.split('***')
        this.task1Label = res[1]
        this.task1OrgDone = true
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
