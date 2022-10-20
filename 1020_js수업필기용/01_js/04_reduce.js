const numbers = [90, 80, 70, 100]

// 배열의 모든 요소의 총 합
const sumNum = numbers.reduce(function (result, number) {
  return result + number
})