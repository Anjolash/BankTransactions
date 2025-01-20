<template>
    <div class="recenttransactionbox">
      <div class="icon-container">
        <img src="../assets/blackarrows.svg" alt="Transaction Icon" />
      </div>
      <div class="transactiondetailscontainer">
        <div class="transactiondetailswords">
          <span>Buy online at {{ transaction.Merchant || "Unknown" }}</span>
          <span class="lowkey">{{ formatDate(transaction["Transaction Date"]) }}</span>
        </div>
        <div class="transactiondetailsamount">
          ${{ transaction["Transaction Amount"] }}
        </div>
      </div>
    </div>
  
    <!-- Loading and Error States -->
    <div>
      <div v-if="isLoading" class="loading-container">Loading transactions...</div>
      <div v-else-if="error" class="error-container">{{ error }}</div>
    </div>
  </template>
  
  <script>
  import dayjs from "dayjs";
  
  export default {
    props: {
      transaction: {
        type: Object,
        required: true,
      },
      isLoading: {
        type: Boolean,
        default: false,
      },
      error: {
        type: String,
        default: null,
      },
    },
    methods: {
      
      formatDate(dateString) {
  if (!dateString || !dayjs(dateString).isValid()) return "Invalid Date"; // Validate input
  return dayjs(dateString).format("MMMM D, YYYY"); // Example: "January 12, 2025"
}

    },
  };
  </script>
  
  <style scoped>
  .bigger {
    font-weight: 500;
    color: #183028;
    font-size: 16px;
  }
  
  .transactiondetailscontainer {
    display: flex;
    width: 100%;
    justify-content: space-between;
    text-align: left;
  }
  
  .transactiondetailswords {
    display: flex;
    width: 100%;
    flex-direction: column;
    font-size: 16px;
    font-weight: 600;
    color: #00160d;
  }
  
  .lowkey {
    margin-top: 6px;
    color: #6e887b;
    font-size: 12px;
  }
  
  .transactiondetailsamount {
    justify-content: end;
    text-align: end;
  }
  
  .table1 {
    position: relative;
    width: 100%;
    border-radius: 10px;
    border: solid 1px #e6e8e7;
  }
  
  .table2 {
    width: 100%;
  }
  
  .box {
    display: flex;
    width: auto;
    justify-content: space-between;
    align-items: center;
    padding: 20px;
    font-weight: 600;
    color: #183028;
    border-bottom: solid 1px #e6e8e7;
  }
  
  .box img {
    width: 20px;
  }
  
  .recenttransactionbox {
    display: flex;
    width: auto;
    gap: 10px;
    align-items: center;
    padding: 20px;
    font-weight: 600;
    color: #183028;
    border-bottom: solid 1px #e6e8e7;
  }
  
  .icon-container {
    background-color: #c5e86c;
    padding: 10px 10px;
    border-radius: 50%;
  }
  
  .box2a {
    padding: 10px 15px;
  }
  
  .chart1 {
    width: 100%;
    margin: 0 auto;
  }
  
  .image-container {
    max-width: 100%;
  }
  
  .image-container img {
    width: 100%;
  }
  
  .image-container2 {
    margin: 0 auto;
    max-width: 200px;
    max-height: 10px;
  }
  
  .image-container2 img {
    width: 100%;
    height: 100%;
  }
  </style>
  