<template>
  <!-- <v-card flat class="scrool" max-height="510"> -->
  <!-- <v-card flat class="scrool" max-height="538"> -->
  <v-card flat class="scrool" max-height="560">
    <v-list-item class="font-weight-medium">ImageNet Class</v-list-item>
    <v-list-item v-if="task1targetRed && $store.state.task1imgSelection.length===0">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task1alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-autocomplete
        :items="task1imgItems"
        :search-input.sync="search"
        @input="search=null"
        chips
        clearable
        hide-details
        hide-selected
        item-text="name"
        item-value="label"
        multiple
        solo
        dense
        v-model="$store.state.task1imgSelection"
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
          >(+{{ $store.state.task1imgSelection.length - 3 }} others)</span> -->
        </template>
      </v-autocomplete>
      <!-- {{ $store.state.task1imgSelection }} -->
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item class="font-weight-medium">CNN Model</v-list-item>
    <v-list-item v-if="task1targetRed && $store.state.task1modelSelection.length===0">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task1alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-select
        v-model="$store.state.task1modelSelection"
        :items="task1modelItems"
        chips
        multiple
        solo
        dense
        height="10"
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      >
        <template v-slot:prepend-item>
          <v-list-item ripple @click="task1toggleModel">
            <v-list-item-action>
              <v-icon small color="rgba(18,38,57,1)">{{ task1selectAllModelIcon }}</v-icon>
            </v-list-item-action>
            <v-list-item-content>
              <v-list-item-title>Select All</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-divider class="mt-2"></v-divider>
        </template>
        <template v-slot:selection="{ item, index }">
          <v-chip v-if="index < 1">
            <span>{{ item }}</span>
          </v-chip>
          <span
            v-if="index === 1"
            class="grey--text caption"
          >(+{{ $store.state.task1modelSelection.length - 1 }} others)</span>
        </template>
      </v-select>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item class="font-weight-medium">Visual Explanation</v-list-item>
    <v-list-item v-if="task1targetRed && $store.state.task1expSelection===null">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task1alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-select
        v-model="$store.state.task1expSelection"
        :items="task1expItems"
        chips
        solo
        dense
        height="10"
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      ></v-select>
    </v-list-item>
    <v-divider></v-divider>
    <v-list-item class="font-weight-medium">Comparison Rule</v-list-item>
    <v-list-item v-if="task1targetRed && $store.state.task1compSelection===null">
      <v-icon small color="red">fas fa-exclamation-triangle</v-icon>
      <span class="red--text">{{ task1alertMsg2 }}</span>
    </v-list-item>
    <v-list-item>
      <v-select
        v-model="$store.state.task1compSelection"
        :items="task1compItems"
        chips
        solo
        dense
        height="10"
        color="rgba(18,38,57,1)"
        item-color="rgba(18,38,57,1)"
      ></v-select>
    </v-list-item>
    <!-- <v-divider></v-divider> -->
    <v-list-item>
      <v-container fluid>
        <v-row>
          <v-col>
            <v-tooltip bottom>
              <template v-slot:activator="{ on }">
                <v-btn
                  color="rgba(18,38,57,1)"
                  text
                  @click="task1clearSelection"
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
                  @click="runTask1($store.state.task1modelSelection, $store.state.task1imgSelection, $store.state.task1expSelection, $store.state.task1compSelection)"
                  v-on="on"
                >Run</v-btn>
              </template>
              <span>It might take several seconds to load images.</span>
            </v-tooltip>
          </v-col>
        </v-row>
      </v-container>
    </v-list-item>
    <v-dialog v-model="task1selectionAlert" width="700">
      <v-card width="700">
        <v-card-title>
          <span>{{ task1alertMsg }}</span>
        </v-card-title>
        <v-card-actions>
          <v-btn text @click="task1selectionAlert=false,task1targetRed=true" color="rgba(18,38,57,1)">OK</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-card>
</template>

<script>
import imgData from '@/data/image.js'

export default {
  name: 'task1SideBar',

  data: () => ({
    task1selectionAlert: false,
    task1targetRed: false,
    search: null,
    task1imgItems: [],
    task1modelItems: [
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
    task1expItems: [
      'Grad-CAM',
      'BBMP',
      'Grad-CAM++',
      'Smooth Grad-CAM++',
      'Score-CAM'
    ],
    task1compItems: ['l1', 'mse', 'ssim', 'hashed'],
    task1alertMsg: null,
    task1alertMsg2: 'This part should not be empty!'
  }),

  computed: {
    task1selectAllModelIcon () {
      if (this.$store.state.task1modelSelection.length === this.task1modelItems.length) {
        return 'fas fa-window-close'
      }
      if (
        this.$store.state.task1modelSelection.length > 0 &&
        this.$store.state.task1modelSelection.length !== this.task1modelItems.length
      ) {
        return 'fas fa-minus-square'
      }
      return 'far fa-square'
    }
    // getTask1imgSelection () {
    //   return this.$store.state.task1imgSelection
    // }
  },

  watch: {
    search (val) {
      if (this.task1imgItems.length > 0) return
      this.task1imgItems = imgData
    }
    // getTask1imgSelection (val) {
    //   if (val.length === 0) {
    //     this.$store.state.taskState = 0
    //     this.$socket.send('Ready***' + this.$store.state.viewModelIdx)
    //   } else {
    //     this.$store.state.taskState = 1
    //     this.$socket.send(
    //       'requestTask1Img***' + val
    //     )
    //   }
    // }
  },

  methods: {
    task1toggleModel: function () {
      this.$nextTick(() => {
        if (this.$store.state.task1modelSelection.length === this.task1modelItems.length) {
          this.$store.state.task1modelSelection = []
        } else {
          this.$store.state.task1modelSelection = this.task1modelItems.slice()
        }
      })
    },
    runTask1: function (res1, res2, res3, res4) {
      console.log('WebSocket connection state: ' + this.$socket.readyState)
      if (this.$socket.readyState === 3) {
        this.task1selectionAlert = true
        this.task1alertMsg = 'WRONG! Connection to the server failed!'
      } else if (
        res1.length === 0 ||
        res2 === null ||
        res3 === null ||
        res4 === null
      ) {
        this.task1selectionAlert = true
        this.task1alertMsg = 'WRONG! Please finish the selections first!'
      } else {
        this.task1selectionAlert = false
        this.$store.state.taskState = 1
        this.$socket.send(
          'requestTask1Img***' + res2
        )
      }
    },
    task1clearSelection: function () {
      this.$store.state.task1modelSelection = []
      this.$store.state.task1imgSelection = []
      this.$store.state.task1expSelection = null
      this.$store.state.task1compSelection = null
    }
  }
}
</script>

<style>
.scrool {
  overflow-y: auto
}
</style>
