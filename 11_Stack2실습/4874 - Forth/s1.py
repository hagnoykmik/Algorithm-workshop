import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
    word = input().split()
    stack = []

# 피연산자
    for char in word:
        if char not in '*/+-.':
            stack.append(int(char))

# 연산자
        else:
            if char == '.':                 # . 이면 연산한 결과 출력
                result = stack[-1]
                break

            elif len(stack) >= 2:           # 스택에 연산할 피연산자가 부족할 때
                y = stack.pop()
                x = stack.pop()

                if char == '*':
                    stack.append(x * y)
                elif char == '/':
                    stack.append(x // y)    # 나눗셈인 경우 항상 나누어 떨어진다
                elif char == '+':
                    stack.append(x + y)
                elif char == '-':
                    stack.append(x - y)

            else:                           # 제대로 연산이 진행되지 않을 때
                result = 'error'
                break

    # 연산 후 스택에 하나보다 많이 남아있을 때
    if len(stack) != 1:
        result = 'error'

    print(f'#{tc} {result}')
