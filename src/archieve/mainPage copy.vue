<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="3">
        <v-navigation-drawer permanent width="400">
          <v-tabs background-color="white" color="primary" right>
            <v-tab @click="taskView=1">TASK 1</v-tab>
            <v-tab @click="taskView=2">TASK 2</v-tab>
            <v-tab-item>
              <task1SideBar />
            </v-tab-item>
            <v-tab-item>
              <task2SideBar />
            </v-tab-item>
          </v-tabs>
        </v-navigation-drawer>
      </v-col>
      <v-col cols="9">
        <v-row v-if="$store.state.taskState===1" no-gutters>
          <v-col>
            <exampleExp />
          </v-col>
        </v-row>
        <v-row v-else-if="$store.state.taskState===2" no-gutters>
          <v-col>
            <task1Main />
          </v-col>
        </v-row>
        <v-row v-else-if="$store.state.taskState===3" no-gutters>
          <v-col>
            <task2Main />
          </v-col>
        </v-row>
        <v-row v-else>
          <v-col>
            <!-- <v-row>
              <v-col>
                <nodeChartTotal />
              </v-col>
            </v-row> -->
            <v-row v-if="taskView==1" no-gutters>
              <v-col>
                <task1Features />
              </v-col>
            </v-row>
            <v-row v-else no-gutters>
              <v-col>
                <task2Features />
              </v-col>
            </v-row>
          </v-col>
        </v-row>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import task1SideBar from '@/components/task1SideBar.vue'
import task2SideBar from '@/components/task2SideBar.vue'
import task1Features from '@/components/task1Features.vue'
import task2Features from '@/components/task2Features.vue'
// import nodeChartTotal from '@/components/nodeChartTotal.vue'
import exampleExp from '@/components/exampleExp.vue'
import task1Main from '@/components/task1Main.vue'
import task2Main from '@/components/task2Main.vue'

export default {
  name: 'mainPage',

  components: {
    task1SideBar,
    task2SideBar,
    task1Features,
    task2Features,
    // nodeChartTotal,
    exampleExp,
    task1Main,
    task2Main
  },

  data: () => ({
    taskView: 1
  }),

  mounted () {
  }
}
</script>
