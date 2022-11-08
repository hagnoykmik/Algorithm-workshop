<template>
  <div>
    <input 
      type="text"
      v-model.trim="todoTitle"
      @keyup.enter="createTodo"
    >
  </div>
</template>

<script>
export default {
  name: 'TodoForm',
  data() {    // 입력값을 저장할 데이터
    return {
      todoTitle: null,
    }
  },  
  methods:{   // enter 눌렀을 때 작동될 method작성
    createTodo() {
      // this.$store.dispatch('액션메서드이름', todoTitle: null)
      if (this.todoTitle) {   // 빈칸 아닐때만
        this.$store.dispatch('createTodo', this.todoTitle)
      }
      this.todoTitle = null
    }
  }     
}
</script>

<style>

</style>