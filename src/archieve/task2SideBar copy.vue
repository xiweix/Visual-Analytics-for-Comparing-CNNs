<template>
  <v-card flat class="scrool" max-height="538">
    <v-list-item>
      <span class="font-weight-medium">
        ImageNet Class
        <!-- <br />
        <span class="font-italic font-weight-light overline">Recommend to choose 3 classes</span> -->
      </span>
    </v-list-item>
    <v-list-item v-if="task2targetRed && $store.state.task2imgSelection.length===0">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task2alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-autocomplete
        :items="task2imgItems"
        :search-input.sync="search"
        @input="search=null"
        chips
        clearable
        hide-details
        hide-selected
        item-text="name"
        item-value="label"
        label="Recommend to choose 3 classes."
        multiple
        solo
        v-model="$store.state.task2imgSelection"
        dense
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      >
        <template v-slot:no-data>
          <v-list-item>
            <v-list-item-title>
              eg:
              <strong>beagle</strong>,
              <strong>junco</strong>, etc.
            </v-list-item-title>
          </v-list-item>
        </template>
        <template v-slot:selection="{ attr, on, item, selected }">
          <v-chip v-bind="attr" :input-value="selected" v-on="on">
            <span>{{ item.name.split(',')[0] }}</span>
          </v-chip>
        <!-- <template v-slot:selection="{ attr, on, item, selected, index }">
          <v-chip v-bind="attr" :input-value="selected" v-on="on" v-if="index < 3">
            <span>{{ item.name.split(',')[0] }}</span>
          </v-chip>
          <span
            v-if="index === 3"
            class="grey--text caption"
          >(+{{ $store.state.task2imgSelection.length - 3 }} others)</span> -->
        </template>
      </v-autocomplete>
      <!-- {{ $store.state.task2imgSelection }} -->
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item class="font-weight-medium">CNN Model</v-list-item>
    <v-list-item v-if="task2targetRed && $store.state.task2modelSelection===null">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task2alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-select
        v-model="$store.state.task2modelSelection"
        :items="task2modelItems"
        chips
        label="Select one model to explore."
        solo
        dense
        height="10"
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      ></v-select>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item class="font-weight-medium">Visual Explanation</v-list-item>
    <v-list-item v-if="task2targetRed && $store.state.task2expSelection===null">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task2alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-select
        v-model="$store.state.task2expSelection"
        :items="task2expItems"
        chips
        label="Select a visual explanation method."
        solo
        dense
        height="10"
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      ></v-select>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item>
      <v-container fluid>
        <v-row>
          <v-col>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn
                  color="rgba(18,38,57,1)"
                  text
                  @click="task2clearSelection"
                  v-on="on"
                >RESET</v-btn>
              </template>
              <span>Click to reset selections.</span>
            </v-tooltip>
          </v-col>
          <v-col>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn
                  color="rgba(18,38,57,1)"
                  text
                  @click="runTask2($store.state.task2modelSelection, $store.state.task2imgSelection, $store.state.task2expSelection)"
                  v-on="on"
                >Run</v-btn>
              </template>
              <span>It might take several seconds to load images.</span>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-container>
    </v-list-item>
    <v-dialog v-model="task2selectionAlert" width="700">
      <v-card width="700">
        <v-card-title>
          <span>{{ task2alertMsg }}</span>
        </v-card-title>
        <v-card-actions>
          <v-btn text @click="task2selectionAlert=false,task2targetRed=true" color="rgba(18,38,57,1)">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import imgData from '@/data/image.js'

export default {
  name: 'task2SideBar',

  data: () => ({
    task2selectionAlert: false,
    task2targetRed: false,
    search: null,
    task2imgItems: [],
    task2modelItems: [
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
    task2expItems: [
      'Grad-CAM',
      'BBMP',
      'Grad-CAM++',
      'Smooth Grad-CAM++',
      'Score-CAM'
    ],
    task2compItems: ['l1', 'mse', 'ssim', 'hashed'],
    task2alertMsg: null,
    task2alertMsg2: 'This part should not be empty!'
  }),

  watch: {
    search (val) {
      if (this.task2imgItems.length > 0) return
      this.task2imgItems = imgData
    }
  },

  methods: {
    runTask2: function (res1, res2, res3) {
      console.log('WebSocket connection state: ' + this.$socket.readyState)
      if (this.$socket.readyState === 3) {
        this.task2selectionAlert = true
        this.task2alertMsg = 'WRONG! Connection to the server failed!'
      } else if (
        res1 === null ||
        res2.length === 0 ||
        res3 === null
      ) {
        this.task2selectionAlert = true
        this.task2alertMsg = 'WRONG! Please finish the selections first!'
      } else {
        this.task2selectionAlert = false
        this.$store.state.taskState = 2
        this.$socket.send(
          'runTask2***' + res1 + '***' + res2 + '***' + res3
        )
      }
    },
    task2clearSelection: function () {
      this.$store.state.task2modelSelection = null
      this.$store.state.task2expSelection = null
      this.$store.state.task2imgSelection = []
    }
  }
}
</script>

<style>
.scrool {
  overflow-y: auto
}
</style>
