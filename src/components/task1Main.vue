<template>
  <v-container fluid>
    <v-card>
      <v-card-title>
        <span v-if="task1OrgDone && $store.state.task1OrgPage">Click the image to view the comparison results.</span>
        <v-spacer></v-spacer>
        <v-btn text @click="exitTask1" color="rgba(18,38,57,1)">EXIT TASK</v-btn>
      </v-card-title>
      <!-- <v-row justify="end">
        <v-col v-if="task1OrgDone && $store.state.task1OrgPage" cols="10">
          <v-card-text>Click the image to view the comparison results.</v-card-text>
        </v-col>
        <v-col cols="auto">
          <v-btn text @click="exitTask1" color="rgba(18,38,57,1)">EXIT TASK</v-btn>
        </v-col>
      </v-row> -->
      <!-- <v-card class="scrool" max-height="654"> -->
      <v-card class="scrool" max-height="1000">
      <!-- <v-card class="scrool" max-height="1200"> -->
        <v-row v-if="$store.state.task1OrgPage">
          <v-col>
            <v-row v-for="task1ImgList in task1OrgImg" :key="task1ImgList.idx">
              <v-col>
                <v-row>
                  <v-col>
                    <v-card-text>The Label is <strong>"{{ task1ImgList.label }}"</strong>. </v-card-text>
                  </v-col>
                </v-row>
                <v-row>
                  <v-col v-for="orgImg in task1ImgList.image" :key="orgImg.id">
                    <v-img v-if="task1OrgDone" @click="requestTask1Exp(orgImg.name, orgImg.img, task1ImgList.label, $store.state.task1modelSelection, $store.state.task1expSelection, $store.state.task1compSelection)" :src="orgImg.img" height="150" width="150" contain>
                    <!-- <v-img v-if="task1OrgDone" @click="requestTask1Exp(orgImg.id, orgImg.img, task1ImgList.idx)" :src="orgImg.img" height="150" width="150" contain> -->
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
              </v-col>
            </v-row>
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
    task1OrgDone: false
  }),

  methods: {
    initTask1: function () {
      this.task1OrgImg = []
      this.task1OrgDone = false
      this.$store.state.task1OrgPage = true
      this.$store.state.task1curImg = null
      this.$store.state.task1curSimM = null
    },

    requestTask1Exp: function (res1, res2, res3, res4, res5, res6) {
      this.$store.state.task1OrgPage = false
      this.$store.state.task1curImg = res2
      this.$socket.send('requestTask1Exp***' + res1 + '***' + res3 + '***' + res4 + '***' + res5 + '***' + res6)
      console.log('request explanation for task 1, img name: ' + res1)
    },

    exitTask1: function () {
      this.$store.state.taskState = 0
      // this.$socket.send('Ready')
      this.$socket.send('Ready***' + this.$store.state.viewModelIdx + '***' + '0.0')
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
        const task1OrgList = []
        const task1OrgListLength = parseInt(res[3])
        let i = 0
        for (i = 0; i < task1OrgListLength; i++) {
          task1OrgList.push({ id: i, img: 'data:image/png;base64,' + res[4 + 2 * i], name: res[5 + 2 * i] })
        }
        this.task1OrgImg.push({ idx: res[1], label: res[2], image: task1OrgList })
      } else if (res.indexOf('task1ImgDone***') !== -1) {
        res = res.split('***')
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
