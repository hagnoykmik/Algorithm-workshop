import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    t = int(input())
    word = input()
    stack = []
    result = ''

# 1. 후위표기법
    for token in word:
        # 연산자일 때
        if token in '*+':
            # 비어있을 때
            if not stack:
                stack.append(token)

            # 다른 연산자일 때
            elif token == '*':
                while stack and stack[-1] == '*':
                    result += stack.pop()
                stack.append(token)

            elif token == '+':
                while stack:
                    result += stack.pop()
                stack.append(token)

        # 피연산자일 때
        else:
            result += token

    # 혹시 스택에 남아 있다면 모두 결과값에 담음
    while stack:
        result += stack.pop()


# 2. 연산
    for char in result:
        # 피연산자일 때
        if char not in '*+':
            stack.append(int(char))

        # 연산자 일 때
        else:
            y = stack.pop()
            x = stack.pop()

            if char == '*':
                stack.append(x * y)
            elif char == '+':
                stack.append(x + y)

    print(f'#{tc} {stack[-1]}')