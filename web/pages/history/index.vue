<template>
  <div class="container">
    <div class="feelings">
      <span class="feelings__title" @click="isClicked">감정 그래프 보기</span>
      <div v-if="chartFlag" class="feelings__chart">
        <bar-chart
          :data="chartData"
          :options="barChartOptions"
          class="chart"
        ></bar-chart>
      </div>
    </div>
    <div class="calendar">
      <span class="calendar__title">지난 일기 보기</span>
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
      chartFlag: false,
    }
  },
  methods: {
    goDetail(day) {
      this.$router.push(`history/${day.id}`)
    },
    isClicked() {
      this.chartFlag = !this.chartFlag
    },
  },
}
</script>

<style lang="scss" scoped>
.container {
  box-sizing: border-box;
  height: $page-height;
  padding: 16px;
  overflow-y: scroll;

  .feelings {
    box-sizing: border-box !important;
    width: 100%;
    padding: 8px 0;
    border-radius: 5px;
    margin-bottom: 16px !important;

    &__title {
      font-size: $heading;
      font-weight: bold;
      margin-bottom: 16px !important;
    }

    &__chart {
      display: flex;
      justify-content: center;
      height: 200px;
    }

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

    &__title {
      font-size: 24px;
      font-weight: bold;
    }
  }
}
</style>
