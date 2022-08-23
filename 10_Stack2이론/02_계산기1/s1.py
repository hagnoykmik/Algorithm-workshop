import sys
sys.stdin = open('')

t = int(input())
for tc in range(1, t + 1):
    word = input()
    stack = []

    # 1. 피연산자는 스택에 push
    for char in word:
        if char not in '*/+-':
            stack.append(int(char))

        # 2. 연산자를 만나면 필요한 만큼(처음엔 2개)의 피연산자를 pop하여 연산
        else:
            x = stack.pop()  # 먼저꺼낸 값이 연산자의 오른쪽
            y = stack.pop()
            # 연산한 결과값 다시 스택에 push
            if char == '+':
                stack.append(y + x)
            elif char == '-':
                stack.append(y - x)
            elif char == '*':
                stack.append(y * x)
            elif char == '/':
                stack.append(y / x)

    # 3. 더 이상 수식이 없으면 종료 + 스택 pop
    print(f'#{tc} {stack[-1]}')

