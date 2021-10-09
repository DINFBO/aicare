<template>
  <div class="delete-modal-overlay">
    <div class="delete-modal">
      <h1>정말 삭제하시겠습니까?</h1>
      <div class="action">
        <button @click="$emit('delete')">네</button>
        <button @click="$emit('cancel')">아니오</button>
      </div>
    </div>
  </div>
</template>
<script>
export default {}
</script>
<style lang="scss" scoped>
.delete-modal-overlay {
  position: fixed;
  top: 0;
  bottom: 0;
  left: 0;
  right: 0;
  display: flex;
  justify-content: center;
  align-items: center;
  background-color: #000000da;

  .delete-modal {
    text-align: center;
    background-color: $white;
    padding: 40px 24px;
    border-radius: 10px;

    h1 {
      font-size: $sub-heading;
      font-weight: bold;
    }

    .action {
      margin-top: 24px;
      display: flex;
      justify-content: space-around;

      button {
        padding: 8px 12px;
        border-radius: 8px;
      }
      button:first-child {
        border: 1px solid $success;
        color: $success;
      }
      button:last-child {
        border: 1px solid $fail;
        color: $fail;
      }
    }
  }
}
</style>
