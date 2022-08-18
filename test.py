def func():
    print(f'함수에서 a의 id는 {id(a)}')
    print(f'함수에서 x의 값{a}')


a = [1, 2, 3]
func(a)

print(f'함수에서 a의 id는 {id(a)}')
print(f'함수에서 x의 값{a}')