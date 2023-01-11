<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="2">
        <v-navigation-drawer permanent width="100%">
          <scatterChartModel :id="$store.state.viewModel" :dataPoint="scatterModelInfo[$store.state.viewModelIdx]"/>
          <v-card flat>
            <v-tabs background-color="white" color="rgba(18,38,57,1)" fixed-tabs>
              <v-tab @click="taskView=1">TASK 1</v-tab>
              <v-tab @click="taskView=2">TASK 2</v-tab>
              <v-tab-item>
                <task1SideBar />
              </v-tab-item>
              <v-tab-item>
                <task2SideBar />
              </v-tab-item>
            </v-tabs>
          </v-card>
        </v-navigation-drawer>
      </v-col>
      <v-col cols="10">
      <!-- <v-col cols="12"> -->
        <OverallFeatures />
        <v-row no-gutters>
          <v-col cols="10">
          <!-- <v-col cols="12"> -->
            <v-row v-if="$store.state.taskState===1" no-gutters>
              <v-col>
                <task1Main />
              </v-col>
            </v-row>
            <v-row v-else-if="$store.state.taskState===2" no-gutters>
              <v-col>
                <task2Main />
              </v-col>
            </v-row>
            <v-row v-else no-gutters>
              <v-col>
                <exampleExp :curModel="$store.state.viewModel"/>
              </v-col>
            </v-row>
          </v-col>
          <v-col cols="2" v-if="taskView===1">
            <task1LabelFeatures />
          </v-col>
          <v-col cols="2" v-else>
            <task2LabelFeatures />
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import scatterChartModel from '@/components/scatterChartModel.vue'
import task1SideBar from '@/components/task1SideBar.vue'
import task2SideBar from '@/components/task2SideBar.vue'
import OverallFeatures from '@/components/OverallFeatures.vue'
import task1LabelFeatures from '@/components/task1LabelFeatures.vue'
import task2LabelFeatures from '@/components/task2LabelFeatures.vue'
import exampleExp from '@/components/exampleExp.vue'
import task1Main from '@/components/task1Main.vue'
import task2Main from '@/components/task2Main.vue'
import scatterModel from '@/data/scatterModel.js'

export default {
  name: 'mainPage',

  components: {
    scatterChartModel,
    task1SideBar,
    task2SideBar,
    OverallFeatures,
    task1LabelFeatures,
    task2LabelFeatures,
    exampleExp,
    task1Main,
    task2Main
  },

  data: () => ({
    taskView: 1,
    scatterModelInfo: scatterModel.scatterInfo
  }),

  mounted () {
    // console.log('main page:' + this.$socket.readyState)
    this.$options.sockets.onmessage = res => {
      res = res.data
      if (res.indexOf('READY') !== -1) {
        this.$socket.send('Ready***' + this.$store.state.viewModelIdx + '***' + '0.0')
      }
    }
  }
}
</script>
