<template>
  <div :id="id" style="width:220px; height: 150px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/bar'

export default {
  name: 'supBarChart2',

  data: () => ({
    id: 'supbar2',
    option: {
      title: {
        text: 'Mean of Class Accuracy',
        left: '3%',
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
      },
      grid: {
        left: 38,
        right: 38,
        top: 30,
        bottom: 36
      },
      xAxis: {
        type: 'category',
        axisLabel: {
          interval: 0
        },
        axisTick: {
          alignWithLabel: true
        },
        data: ['995', '255', '139', '899', '782', '885'],
        name: 'class',
        nameLocation: 'middle',
        nameGap: 25
      },
      yAxis: {
        type: 'value',
        name: 'Mean',
        nameLocation: 'middle',
        nameGap: 25
      },
      series: [
        {
          name: 'Accuracy',
          type: 'bar',
          barWidth: '60%',
          data: [98.769, 97.692, 97.385, 26.154, 16.000, 15.692]
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
    }
  }
}
</script>

<style scoped>
.echarts {
  width: 220px;
  height: 150px;
}
</style>
