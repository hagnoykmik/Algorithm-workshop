const arr = [1, 2, 3, 4, 5]

// 1단계
const result = arr.find(function (elem) {
  return elem % 2 === 0
})

// 2단계
const result = arr.find((elem) => {
  return elem % 2 === 0
})

// 3단계
const result = arr.some((elem) => elem % 2 === 0)

// every
const result = arr.every((elem) => elem % 2 === 0)