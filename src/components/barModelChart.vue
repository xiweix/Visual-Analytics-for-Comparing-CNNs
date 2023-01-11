<template>
  <!-- <div :id="id" style="width: 370px; height: 200px" class="echarts"></div> -->
  <div :id="id" style="width: 470px; height: 200px" class="echarts"></div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/bar'
import barData from '@/data/barData.js'

export default {
  name: 'barModelChart',

  props: {
    id: {
      style: String,
      default: 'barModelChartTest'
    },
    modelIdx: {
      style: Number,
      default: 0
    },
    modelName: {
      style: String,
      default: 'mobilenet_v2'
    }
  },

  data: () => ({
    chart: null,
    totalData: barData.barModelInfo,
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
        text: 'Model: mobilenet_v2',
        left: 10,
        textStyle: {
          fontSize: 15
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
        // formatter: function (param) {
        //   // return param.name + '<br />Accuracy: ' + param.value + '%'
        //   return param.name
        // }
      },
      grid: {
        left: 50,
        right: 50,
        top: 50,
        bottom: 50
      },
      dataZoom: [{
        type: 'inside'
      }, {
        type: 'slider'
      }],
      xAxis: {
        type: 'category',
        // axisLabel: {
        //   interval: 0
        // },
        axisTick: {
          alignWithLabel: true
        },
        data: barData.barModelInfo[0].labelList,
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
          data: barData.barModelInfo[0].labelAcc
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
        console.log(params)
      })
    }
  },
  watch: {
    modelIdx: {
      handler (newVal, oldVal) {
        if (this.chart) {
          var curTitle = this.modelName
          var curData = this.totalData[newVal]
          this.option.title.text = 'Model: ' + curTitle
          // console.log(this.option.color)
          var curcolor = []
          curcolor.push(this.totalColors[newVal])
          this.option.color = curcolor
          // console.log(this.option.color)
          this.option.xAxis.data = curData.labelList
          this.option.series.data = curData.labelAcc
          this.chart.setOption(this.option)
        }
      }
    }
  }
}
</script>
