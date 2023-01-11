<template>
  <div :id="id" style="width:220px; height: 200px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/scatter'
import scatterData from '@/data/scatterData.js'

export default {
  name: 'labelScatterChart',

  props: {
    id: {
      style: String,
      default: 'main'
    },
    dataPoint: {
      style: Object,
      default: function () { return scatterData.labelInfo[0] }
    }
  },

  data: () => ({
    chart: null,
    option: {
      title: {
        text: 'Class 0 Information',
        // left: '3%',
        itemGap: 5,
        textStyle: {
          fontSize: 15
        },
        subtext: 'Name: tench',
        subtextStyle: {
          fontSize: 12,
          color: 'grey'
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
        left: 44,
        right: 44,
        top: 50,
        bottom: 60
      },
      series: [
        {
          data: scatterData.labelInfo[0].content[0],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(75,120,155,1)'
        },
        {
          data: scatterData.labelInfo[0].content[1],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(150,45,73,1)'
        },
        {
          data: scatterData.labelInfo[0].content[2],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(230,165,127,1)'
        },
        {
          data: scatterData.labelInfo[0].content[3],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(250,188,60,1)'
        },
        {
          data: scatterData.labelInfo[0].content[4],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(128,196,169,1)'
        },
        {
          data: scatterData.labelInfo[0].content[5],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(0,153,102,1)'
        },
        {
          data: scatterData.labelInfo[0].content[6],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(89,70,112,1)'
        },
        {
          data: scatterData.labelInfo[0].content[7],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(216,118,120,1)'
        },
        {
          data: scatterData.labelInfo[0].content[8],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(190,114,73,1)'
        },
        {
          data: scatterData.labelInfo[0].content[9],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(149,128,74,1)'
        },
        {
          data: scatterData.labelInfo[0].content[10],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(45,83,96,1)'
        },
        {
          data: scatterData.labelInfo[0].content[11],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(89,60,80,1)'
        },
        {
          data: scatterData.labelInfo[0].content[12],
          type: 'scatter',
          symbolSize: 5,
          color: 'rgba(237,122,158,1)'
        }
      ]
    }
  }),

  mounted () {
    this.init(this.dataPoint)
  },

  methods: {
    init (res) {
      if (res) {
        // console.log('original: ' + this.chart)
        this.chart = echarts.init(document.getElementById(this.id))
        var label = res.label
        var labelName = res.labelname
        this.option.title.text = 'Class ' + label + ' Information'
        this.option.title.subtext = 'Name: ' + labelName
        var datas = res.content
        let i = 0
        for (i = 0; i < datas.length; i++) {
          // console.log('old---' + this.option.series[i].data)
          this.option.series[i].data = datas[i]
          // console.log('new---' + this.option.series[i].data)
        }
        this.chart.setOption(this.option)
        // console.log('after init and set value: ' + this.chart)
      } else {
        // console.log('original: ' + this.chart)
        this.chart = echarts.init(document.getElementById(this.id))
        this.chart.setOption(this.option)
        // console.log('after init: ')
      }
    }
  },

  watch: {
    dataPoint: {
      handler (newVal, oldVal) {
        if (this.chart) {
          if (newVal) {
            var label = newVal.label
            var labelName = newVal.labelname
            this.option.title.text = 'Class ' + label + ' Information'
            this.option.title.subtext = 'Name: ' + labelName
            var datas = newVal.content
            let i = 0
            for (i = 0; i < datas.length; i++) {
              console.log('old---' + this.option.series[i].data)
              this.option.series[i].data = datas[i]
              console.log('new---' + this.option.series[i].data)
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
