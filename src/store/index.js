import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    taskState: 0,
    task1modelSelection: [],
    task1imgSelection: [],
    task1expSelection: null,
    task1compSelection: null,
    task1OrgPage: true,
    task1curImg: null,
    task1curSimM: null,
    task1ExpRes: [],
    task1search: '',
    task1TableReceive: false,
    task2imgSelection: [],
    task2expSelection: null,
    task2modelSelection: null,
    viewModel: 'mobilenet_v2',
    viewModelIdx: 0,
    viewLabel: 'animal',
    viewLabelIdx: 0
  },
  mutations: {
  },
  actions: {
  },
  modules: {
  }
})
