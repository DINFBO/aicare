<template>
  <div class="container">
    <div class="feelings">
      <bar-chart :data="chartData" :options="barChartOptions" class="chart"></bar-chart>
    </div>
    <div class="calendar">
      <no-ssr>
        <v-calendar
          :attributes="attrs"
          mode="date"
          is-expanded
          @dayclick="goDetail"
        />
      </no-ssr>
    </div>
  </div>
</template>

<script>
import BarChart from '~/components/BarChart'

export default {
  components: {
    BarChart,
  },
  data() {
    return {
      attrs: [
        {
          key: 'today',
          highlight: {
            style: {
              background: '#E6C823',
            },
            contentStyle: {
              color: '#ffffff',
            },
          },
          dates: new Date(),
        },
        {
          key: 'writeDay',
          dot: true,
          dates: [],
        },
      ],
      chartData: {
        labels: ['우울', '기쁨', '분노'],
        datasets: [
          {
            backgroundColor: ['red', 'blue', 'green'],
            data: [4, 6, 3],
          },
        ],
      },
      barChartOptions: {
        responsive: true,
        maintainAspectRatio: false,
        legend: {
          display: false,
        },
        title: {
          display: true,
          text: '감정 빈도',
        },
        scales: {
          xAxes: [
            {
              gridLines: { display: false, drawBorder: false },
              ticks: {
                beginAtZero: true,
                stepSize: 5,
              },
              min: 0,
              max: 31,
            },
          ],
          yAxes: [
            {
              gridLines: { drawBorder: false, display: false },
              barPercentage: 0.3,
            },
          ],
        },
      },
    }
  },
  methods: {
    goDetail(day) {
      this.$router.push(`history/${day.id}`)
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: calc(100vh - 57px - 47px);
  padding: 16px;
  overflow-y: scroll;

  .feelings {
    box-sizing: border-box !important;
    font-weight: bold;
    display: flex;
    justify-content: center;

    height: 200px;
    width: 100%;

    .chart {
      width: 100%;
    }
  }

  .calendar {
    &::v-deep .vc-container {
      border: none;
      border-radius: 5px;

      .vc-header {
        padding: 20px 18px;
      }
      .vc-weekday {
        color: $black;
      }
      .vc-day {
        padding: 20px 0;
        color: $gray-darken;
      }
    }
  }
}
</style>
