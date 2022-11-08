import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    todos: [
      {
        title: '할 일을 추가하세요',
        isCompleted: false,
      },
    ]
  },
  getters: {
  },
  mutations: {
    CREATE_TODO(state, todoItem) {
      state.todos.push(todoItem)
    },
    DELETE_TODO(state, todoItem) {
      const index = state.todos.indexOf(todoItem)  // 몇번째 요소인지 찾기
      state.todos.splice(index, 1)
    }
  },
  actions: {
    createTodo(context, todoTitle) {
      // todo 객체 만들기
      const todoItem = {
        title: todoTitle,
        isCompleted: false,
      }
      // console.log(todoItem)
      context.commit('CREATE_TODO', todoItem)
    },
    deleteTodo(context, todoItem) {
      // actions에서 할 일이 없음 -> 생략
      context.commit('DELETE_TODO', todoItem)
    }
  },
  modules: {
  }
})
