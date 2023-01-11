<template>
  <v-container fluid>
    <v-row no-gutters>
      <v-col cols="2">
        <v-navigation-drawer permanent width="400">
          <v-tabs background-color="white" color="rgba(27,36,49,1)" right>
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
      <v-col cols="10">
        <v-row no-gutters>
          <v-col>
            <OverallFeatures />
          </v-col>
        </v-row>
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
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import task1SideBar from '@/components/task1SideBar.vue'
import task2SideBar from '@/components/task2SideBar.vue'
import OverallFeatures from '@/components/OverallFeatures.vue'
import exampleExp from '@/components/exampleExp.vue'
import task1Main from '@/components/task1Main.vue'
import task2Main from '@/components/task2Main.vue'

export default {
  name: 'mainPage',

  components: {
    task1SideBar,
    task2SideBar,
    OverallFeatures,
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
