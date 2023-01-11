<template>
  <div id='test' style="width: 550px; height: 200px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/radar'

export default {
  name: 'radarChart',

  data: () => ({
    chart: null,
    option: {
      tooltip: {
        trigger: 'item',
        // confine: true,
        triggerOn: 'mousemove',
        position: 'bottom',
        textStyle: {
          fontSize: 10
        }
      },
      grid: {
        left: 20,
        top: 0,
        right: 0,
        bottom: 0
      },
      legend: {
        type: 'scroll',
        orient: 'vertical',
        right: 60,
        itemGap: 0,
        itemWidth: 5,
        textStyle: {
          fontSize: 10
        },
        data: [
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
        selectedMode: 'multiple',
        selected: {
          mobilenet_v2: true,
          alexnet: false,
          resnet18: false,
          resnet34: false,
          resnet50: false,
          resnet101: false,
          resnet152: false,
          densenet121: false,
          densenet161: false,
          densenet169: false,
          densenet201: false,
          squeezenet1_1: false,
          shufflenet_v2_x0_5: false
        }
      },
      radar: {
        name: {
          textStyle: {
            color: 'black'
          }
        },
        center: ['41%', '50%'],
        indicator: [
          { name: 'animal', min: 50, max: 100 },
          { name: 'artifact', min: 50, max: 100 },
          { name: 'misc', min: 50, max: 100 },
          { name: 'natural object', min: 50, max: 100 },
          { name: 'geological formation', min: 50, max: 100 },
          { name: 'person', min: 50, max: 100 },
          { name: 'plant', min: 50, max: 100 },
          { name: 'fungus', min: 50, max: 100 }
          // { name: 'animal, animate being, beast, brute, creature, fauna', max: 100 },
          // { name: 'artifact, artefact', max: 100 },
          // { name: 'misc', max: 100 },
          // { name: 'natural object', max: 100 },
          // { name: 'geological formation, formation', max: 100 },
          // { name: 'person, individual, someone, somebody, mortal, soul', max: 100 },
          // { name: 'plant, flora, plant life', max: 100 },
          // { name: 'fungus', max: 100 }
        ],
        nameGap: 5,
        shape: 'polygon',
        scale: true,
        triggerEvent: true
      },
      series: [{
        type: 'radar',
        data: [
          {
            value: [79.682, 67.169, 68.48, 76.889, 66.714, 79.0, 98.0, 86.0],
            name: 'mobilenet_v2',
            itemStyle: {
              color: 'rgba(75,120,155,1)'
            },
            lineStyle: {
              color: 'rgba(75,120,155,1)'
            }
          },
          {
            value: [66.266, 50.586, 55.025, 67.148, 57.571, 62.5, 97.0, 74.0],
            name: 'alexnet',
            itemStyle: {
              color: 'rgba(150,45,73,1)'
            },
            lineStyle: {
              color: 'rgba(150,45,73,1)'
            }
          },
          {
            value: [78.117, 64.722, 66.268, 74.333, 63.429, 77.0, 97.0, 82.0],
            name: 'resnet18',
            itemStyle: {
              color: 'rgba(230,165,127,1)'
            },
            lineStyle: {
              color: 'rgba(230,165,127,1)'
            }
          },
          {
            value: [81.472, 68.62, 69.657, 78.741, 67.0, 79.0, 98.0, 86.0],
            name: 'resnet34',
            itemStyle: {
              color: 'rgba(250,188,60,1)'
            },
            lineStyle: {
              color: 'rgba(250,188,60,1)'
            }
          },
          {
            value: [83.83, 71.927, 73.278, 80.185, 69.429, 79.0, 97.0, 84.0],
            name: 'resnet50',
            itemStyle: {
              color: 'rgba(128,196,169,1)'
            },
            lineStyle: {
              color: 'rgba(128,196,169,1)'
            }
          },
          {
            value: [84.644, 73.689, 74.768, 77.778, 69.714, 80.5, 99.0, 86.0],
            name: 'resnet101',
            itemStyle: {
              color: 'rgba(0,153,102,1)'
            },
            lineStyle: {
              color: 'rgba(0,153,102,1)'
            }
          },
          {
            value: [85.611, 74.854, 74.177, 78.518, 69.714, 82.5, 98.0, 86.0],
            name: 'resnet152',
            itemStyle: {
              color: 'rgba(89,70,112,1)'
            },
            lineStyle: {
              color: 'rgba(89,70,112,1)'
            }
          },
          {
            value: [82.988, 69.99, 70.843, 78.037, 67.143, 76.0, 98.0, 86.0],
            name: 'densenet121',
            itemStyle: {
              color: 'rgba(216,118,120,1)'
            },
            lineStyle: {
              color: 'rgba(216,118,120,1)'
            }
          },
          {
            value: [84.817, 73.421, 72.323, 78.741, 71.143, 78.5, 98.0, 80.0],
            name: 'densenet161',
            itemStyle: {
              color: 'rgba(190,114,73,1)'
            },
            lineStyle: {
              color: 'rgba(190,114,73,1)'
            }
          },
          {
            value: [83.508, 71.675, 72.783, 78.074, 65.857, 74.0, 100.0, 86.0],
            name: 'densenet169',
            itemStyle: {
              color: 'rgba(149,128,74,1)'
            },
            lineStyle: {
              color: 'rgba(149,128,74,1)'
            }
          },
          {
            value: [84.111, 73.272, 73.798, 79.111, 71.857, 83.0, 99.0, 86.0],
            name: 'densenet201',
            itemStyle: {
              color: 'rgba(45,83,96,1)'
            },
            lineStyle: {
              color: 'rgba(45,83,96,1)'
            }
          },
          {
            value: [68.188, 51.782, 57.884, 66.148, 59.571, 65.0, 95.0, 82.0],
            name: 'squeezenet1_1',
            itemStyle: {
              color: 'rgba(89,60,80,1)'
            },
            lineStyle: {
              color: 'rgba(89,60,80,1)'
            }
          },
          {
            value: [70.227, 54.73, 59.641, 71.259, 59.714, 67.5, 98.0, 82.0],
            name: 'shufflenet_v2_x0_5',
            itemStyle: {
              color: 'rgba(237,122,158,1)'
            },
            lineStyle: {
              color: 'rgba(237,122,158,1)'
            }
          }
        ]
      }]
    }
  }),

  mounted () {
    this.init()
  },

  methods: {
    mapModel (modelName) {
      const m = new Map()
      m.set('mobilenet_v2', 0)
      m.set('alexnet', 1)
      m.set('resnet18', 2)
      m.set('resnet34', 3)
      m.set('resnet50', 4)
      m.set('resnet101', 5)
      m.set('resnet152', 6)
      m.set('densenet121', 7)
      m.set('densenet161', 8)
      m.set('densenet169', 9)
      m.set('densenet201', 10)
      m.set('squeezenet1_1', 11)
      m.set('shufflenet_v2_x0_5', 12)
      return m.get(modelName)
    },
    mapLabel (labelName) {
      const m = new Map()
      m.set('animal', 0)
      m.set('artifact', 1)
      m.set('misc', 2)
      m.set('natural object', 3)
      m.set('geological formation', 4)
      m.set('person', 5)
      m.set('plant', 6)
      m.set('fungus', 7)
      return m.get(labelName)
    },
    init () {
      this.chart = echarts.init(document.getElementById('test'))
      this.chart.setOption(this.option)
      this.chart.on('click', (params) => {
        if (params.componentType === 'radar') {
          console.log(params.name)
          this.$store.state.viewLabel = params.name
          this.$store.state.viewLabelIdx = this.mapLabel(params.name)
        } else if (params.componentType === 'series') {
          // console.log('model: ' + params.name)
          this.$store.state.viewModel = params.name
          this.$store.state.viewModelIdx = this.mapModel(params.name)
        }
      })
    }
  }
}
</script>
