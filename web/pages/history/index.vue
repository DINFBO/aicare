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
      <Calendar />
    </div>
  </div>
</template>

<script>
import Calendar from '../../components/Calendar.vue'
import BarChart from '~/components/BarChart'

export default {
  components: {
    BarChart,
    Calendar,
  },
  data() {
    return {
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
    &__title {
      font-size: 24px;
      font-weight: bold;
    }
  }
}
</style>
