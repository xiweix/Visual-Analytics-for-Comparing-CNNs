<template>
  <div :id="id" style="width: 370px; height: 200px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/bar'
import barData from '@/data/barData.js'

export default {
  name: 'barLabelChart',

  props: {
    id: {
      style: String,
      default: 'barLabelChartTest'
    },
    modelIdx: {
      style: Number,
      default: 0
    },
    modelName: {
      style: String,
      default: 'mobilenet_v2'
    },
    parentIdx: {
      style: Number,
      default: 0
    },
    parentName: {
      style: String,
      default: 'animal'
    }
  },

  data: () => ({
    chart: null,
    totalData: barData.barLabelInfo,
    totalColors: [
      'rgba(75,120,155,1)',
      'rgba(150,45,73,1)',
      'rgba(230,165,127,1)',
      'rgba(250,188,60,1)',
      'rgba(128,196,169,1)',
      'rgba(0,153,102,1)',
      'rgba(89,70,112,1)',
      'rgba(216,118,120,1)',
      'rgba(190,114,73,1)',
      'rgba(149,128,74,1)',
      'rgba(45,83,96,1)',
      'rgba(89,60,80,1)',
      'rgba(237,122,158,1)'
    ],
    option: {
      title: {
        text: 'Root Class: animal',
        left: 10,
        itemGap: 7,
        textStyle: {
          fontSize: 15
        },
        subtext: 'Model: mobilenet_v2',
        subtextStyle: {
          fontSize: 12,
          color: 'grey'
        }
      },
      color: ['rgba(75,120,155,1)'],
      tooltip: {
        trigger: 'axis',
        confine: true,
        axisPointer: {
          type: 'shadow'
        },
        textStyle: {
          fontSize: 10
        }
      },
      grid: {
        left: 50,
        right: 50,
        top: 50,
        bottom: 50
      },
      xAxis: {
        type: 'category',
        // axisLabel: {
        //   interval: 0
        // },
        axisTick: {
          alignWithLabel: true
        },
        data: barData.barLabelInfo[0].modelsInfo[0].labelList,
        name: 'class',
        nameLocation: 'middle',
        nameGap: 25
      },
      yAxis: {
        type: 'value',
        name: 'Accuracy (%)',
        nameLocation: 'middle',
        nameGap: 25
      },
      series: [
        {
          name: 'Accuracy',
          type: 'bar',
          barWidth: '60%',
          data: barData.barLabelInfo[0].modelsInfo[0].labelAcc
        }
      ]
    }
  }),

  mounted () {
    this.init()
  },

  methods: {
    init () {
      this.chart = echarts.init(document.getElementById(this.id))
      this.chart.setOption(this.option)
      this.chart.on('click', function (params) {
        console.log(params.value)
      })
    },
    updateValue () {
      var curTitle = this.parentName
      var curSubTitle = this.modelName
      var curData = this.totalData[this.parentIdx].modelsInfo[this.modelIdx]
      this.option.title.text = 'Root Class: ' + curTitle
      this.option.title.subtext = 'Model: ' + curSubTitle
      var curcolor = []
      curcolor.push(this.totalColors[this.modelIdx])
      this.option.color = curcolor
      this.option.xAxis.data = curData.labelList
      this.option.series.data = curData.labelAcc
      this.chart.setOption(this.option)
    }
  },
  watch: {
    modelIdx: {
      handler (newVal, oldVal) {
        if (this.chart) {
          this.updateValue()
        }
      }
    },
    parentIdx: {
      handler (newVal, oldVal) {
        if (this.chart) {
          this.updateValue()
        }
      }
    }
  }
}
</script>
