<template>
  <div>
    {{ todo.title }}
    <button @click="deleteTodo">Delete</button>
  </div>
</template>

<script>
export default {
  name: 'TodoListItem',
  props: {
    todo: Object,
  },
  methods: {           // delete를 누르면 실행될 method
    deleteTodo() {
      // console.log('삭제 메서드 호출!!')
      this.$store.dispatch('deleteTodo', this.todo)  // 삭제할거 (this.todo=todo: Object) 
      // deleteTodo 액션 호출
    }
  }
}
</script>

<style>

</style>