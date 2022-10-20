

// 함수 선언식
// function add(num1, num2) {
//   return num1 + num2
// }

// console.log(add(2, 7))




// 함수 표현식
// const add = function(num1, num2) {
//   return num1 + num2
// }

// console.log(add(2, 7))


// const numbers = [1,2,3,4,5]
// let sum_number = 0

// for (const num of numbers) {
//   sum_number += num
// }

// console.log(sum_number)


// const greeting = function (name) {
//   return `Hi ${name}`
// }
// console.log(greeting())


// const threeArgs = function (arg1, arg2, arg3) {
//   return [arg1, arg2, arg3]
// }

// console.log(threeArgs(1))

// let parts = ['shoulders', 'knees']
// let lyrics = ['head', ...parts, 'and', 'toes']

// console.log(lyrics)

// const rest0pr = function (arg1, arg2, ...restArgs) {
//   return [arg1, arg2, restArgs]
// }

// console.log(rest0pr(1, 2))

// let star = '*'
// for (let i = 1; i < 6; i++) {
//   console.log(star)
//   star += star
// }


const numbers = [1, 2, 3, 4, 5]

console.log(numbers[0])
console.log(numbers[-1])
console.log(numbers.length)
console.log(numbers.length - 1)

numbers.reverse()
console.log(numbers)

numbers.push(100)
console.log(numbers)

numbers.pop()
console.log(numbers)

console.log(numbers.includes(1))
console.log(numbers.includes(100))

console.log(numbers.indexOf(3))

console.log(numbers.join())
console.log(numbers.join(''))
console.log(numbers.join(' '))
console.log(numbers.join('-'))










