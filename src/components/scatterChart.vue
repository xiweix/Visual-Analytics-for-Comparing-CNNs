<template>
  <!-- <div :id="id" style="width:300px; height: 200px" class="echarts"> -->
  <div :id="id" style="width:500px; height: 200px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/scatter'
import scatterData from '@/data/scatterData.js'

export default {
  name: 'scatterChart',

  props: {
    id: {
      style: String,
      default: 'main'
    },
    dataPoint: Object
  },

  data: () => ({
    chart: null,
    option: {
      title: {
        text: 'Overall Information',
        left: '8%',
        textStyle: {
          fontSize: 15
        }
      },
      tooltip: {
        trigger: 'item',
        triggerOn: 'mousemove',
        confine: true,
        formatter: function (param) {
          return param.data[2] + '<br />Accuracy: ' + param.data[1] + '%<br />Param: ' + param.data[0]
        },
        textStyle: {
          fontSize: 10
        }
      },
      xAxis: {
        name: '# of parameters ( * 10^7)',
        nameLocation: 'middle',
        nameGap: 20
        // splitNumber: 4
        // splitLine: {
        //   lineStyle: {
        //     type: 'dashed'
        //   }
        // }
      },
      yAxis: {
        type: 'value',
        name: 'Accuracy (%)',
        nameLocation: 'middle',
        nameGap: 25,
        scale: true
        // splitLine: {
        //   lineStyle: {
        //     type: 'dashed'
        //   }
        // }
      },
      grid: {
        left: 50,
        right: 40,
        top: 50,
        bottom: 50
      },
      series: [
        {
          data: scatterData.overallInfo[0],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(75,120,155,1)'
        },
        {
          data: scatterData.overallInfo[1],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(150,45,73,1)'
        },
        {
          data: scatterData.overallInfo[2],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(230,165,127,1)'
        },
        {
          data: scatterData.overallInfo[3],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(250,188,60,1)'
        },
        {
          data: scatterData.overallInfo[4],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(128,196,169,1)'
        },
        {
          data: scatterData.overallInfo[5],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(0,153,102,1)'
        },
        {
          data: scatterData.overallInfo[6],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(89,70,112,1)'
        },
        {
          data: scatterData.overallInfo[7],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(216,118,120,1)'
        },
        {
          data: scatterData.overallInfo[8],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(190,114,73,1)'
        },
        {
          data: scatterData.overallInfo[9],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(149,128,74,1)'
        },
        {
          data: scatterData.overallInfo[10],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(45,83,96,1)'
        },
        {
          data: scatterData.overallInfo[11],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(89,60,80,1)'
        },
        {
          data: scatterData.overallInfo[12],
          type: 'scatter',
          symbolSize: 7,
          color: 'rgba(237,122,158,1)'
        }
      ]
    }
  }),

  mounted () {
    this.init(this.dataPoint)
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
          this.$store.state.viewModel = params.value[2]
          this.$store.state.viewModelIdx = this.mapModel(params.value[2])
        })
        // console.log('after init and set value: ' + this.chart)
      } else {
        // console.log('original: ' + this.chart)
        // console.log(this.$store.state.viewModel)
        this.chart = echarts.init(document.getElementById(this.id))
        this.chart.setOption(this.option)
        this.chart.on('click', (params) => {
          console.log(params.value)
          this.$store.state.viewModel = params.value[2]
          this.$store.state.viewModelIdx = this.mapModel(params.value[2])
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
