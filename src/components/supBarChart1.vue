<template>
  <div :id="id" style="width:220px; height: 160px" class="echarts">
  </div>
</template>

<script>
import echarts from 'echarts'
import 'echarts/lib/chart/bar'

export default {
  name: 'supBarChart1',

  data: () => ({
    id: 'supbar1',
    option: {
      title: {
        text: 'Range of Class Accuracy',
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
        data: ['124', '596', '676', '27', '24', '275'],
        name: 'class',
        nameLocation: 'middle',
        nameGap: 25
      },
      yAxis: {
        type: 'value',
        name: 'Range',
        nameLocation: 'middle',
        nameGap: 25
      },
      series: [
        {
          name: 'Accuracy',
          type: 'bar',
          barWidth: '60%',
          data: [62, 60, 60, 6, 4, 4]
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
