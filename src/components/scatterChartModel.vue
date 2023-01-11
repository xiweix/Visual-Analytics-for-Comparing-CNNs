<template>
  <!-- <v-card flat class="scrool" max-width="300px" max-height="680px"> -->
  <v-card flat class="scrool" max-width="400px" max-height="500px">
    <!-- <div :id="id" style="width: 300px; height: 660px" class="echarts"> -->
    <div :id="id" style="width: 380px; height: 500px" class="echarts">
    </div>
  </v-card>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/scatter'
import scatterModel from '@/data/scatterModel.js'

export default {
  name: 'scatterChartModel',

  props: {
    id: {
      style: String,
      default: 'scatterModelmain'
    },
    dataPoint: Object
  },

  data: () => ({
    chart: null,
    option: {
      title: {
        text: 'Model: mobilenet_v2',
        textStyle: {
          fontSize: 15
        }
      },
      // brush: {
      //   toolbox: [
      //     'rect',
      //     'polygon',
      //     'keep',
      //     'clear'
      //   ]
      // },
      dataZoom: [
        {
          type: 'inside',
          xAxisIndex: [0],
          yAxisIndex: [0]
        }
      ],
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove',
        confine: true,
        textStyle: {
          fontSize: 12
        },
        formatter: function (param) {
          return 'Class: ' + param.data[4] + '. ' + param.data[2] + '<br />Class Accuracy: ' + param.data[6] + '%<br />Root Class: ' + param.data[3]
        }
      },
      legend: {
        type: 'scroll',
        left: 0,
        bottom: 0,
        // orient: 'vertical',
        selectedMode: 'multiple',
        itemGap: 5,
        itemWidth: 5
      },
      xAxis: {
        type: 'value',
        scale: true,
        show: false,
        splitLine: {
          show: false
        },
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        }
      },
      yAxis: {
        type: 'value',
        scale: true,
        show: false,
        splitLine: {
          show: false
        },
        axisLine: {
          show: false
        },
        axisTick: {
          show: false
        }
      },
      grid: {
        left: 0,
        right: 0,
        top: 20,
        bottom: 15
      },
      series: [
        {
          name: 'animal',
          data: scatterModel.scatterInfo[0].content[0],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(97,154,214,1)'
        },
        {
          name: 'artifact',
          data: scatterModel.scatterInfo[0].content[1],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(137,127,152,1)'
        },
        {
          name: 'misc',
          data: scatterModel.scatterInfo[0].content[2],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(0,255,0,1)'
        },
        {
          name: 'natural object',
          data: scatterModel.scatterInfo[0].content[3],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(27,36,49,1)'
        },
        {
          name: 'geological formation',
          data: scatterModel.scatterInfo[0].content[4],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(255,165,0,1)'
        },
        {
          name: 'person',
          data: scatterModel.scatterInfo[0].content[5],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(255,255,0,1)'
        },
        {
          name: 'plant',
          data: scatterModel.scatterInfo[0].content[6],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(255,0,0,1)'
        },
        {
          name: 'fungus',
          data: scatterModel.scatterInfo[0].content[7],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(0,0,255,1)'
        }
      ]
    }
  }),

  mounted () {
    this.init(this.dataPoint)
  },

  methods: {
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
    init (res) {
      if (res) {
        // console.log('original: ' + this.chart)
        this.chart = echarts.init(document.getElementById(this.id))
        var datas = res.content
        let i = 0
        for (i = 0; i < datas.length; i++) {
          // console.log('old---' + this.option.series[i].data)
          this.option.series[i].data = datas[i]
          // console.log('new---' + this.option.series[i].data)
        }
        this.chart.setOption(this.option)
        this.chart.on('click', (params) => {
          console.log(params.value)
          this.$store.state.viewLabel = params.value[3]
          this.$store.state.viewLabelIdx = this.mapLabel(params.value[3])
        })
        // console.log('after init and set value: ' + this.chart)
      } else {
        // console.log('original: ' + this.chart)
        // console.log(this.$store.state.viewModel)
        this.chart = echarts.init(document.getElementById(this.id))
        this.chart.setOption(this.option)
        this.chart.on('click', (params) => {
          console.log(params.value)
          this.$store.state.viewLabel = params.value[3]
          this.$store.state.viewLabelIdx = this.mapLabel(params.value[3])
        })
        // console.log('after init: ' + this.chart)
      }
    }
  },

  watch: {
    dataPoint: {
      handler (newVal, oldVal) {
        if (this.chart) {
          if (newVal) {
            this.option.title.text = 'Model: ' + this.$store.state.viewModel
            var datas = newVal.content
            let i = 0
            for (i = 0; i < datas.length; i++) {
              // console.log('old---' + this.option.series[i].data)
              this.option.series[i].data = datas[i]
              // console.log('new---' + this.option.series[i].data)
            }
            this.chart.setOption(this.option)
          } else {
            this.chart.setOption(this.option)
          }
        } else {
          this.init(this.dataPoint)
        }
      },
      deep: true
    }
  }
}
</script>

<style>
/* .scrool {
  overflow-y: auto;
  overflow-x: auto
} */
</style>
