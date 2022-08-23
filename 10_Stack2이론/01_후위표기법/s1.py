import sys
sys.stdin = open('')

t = int(input())

for tc in range(1, t + 1):
    word = input()
    result = ''     # 반환 결과
    stack = []

# 1. 연산자일 때
    for token in word:
        if token in '*?+-()':
            # 1) 비어있거나 '('를 만나면 push(연산자 순위 제일 높음)
            if not stack or token == '(':
                stack.append(token)

            # 2)다른 연산자라면 스택 top과 비교해서 더 높으면 push
            # 우선순위와 같거나 낮으면 더 낮은 연산자를 만날 때까지 pop하고 result에 담음
            elif token in '*/':
                while stack and stack[-1] in '*/':         # 만약에 top이 */면 pop 아니면 push
                    result += stack.pop()
                # 이후에 담기
                stack.append(token)

            elif token in '+-':
                while stack and stack[-1] != '(':          # +-보다 낮은건 열린괄호밖에 없으므로 열린괄호일때만 push
                    result += stack.pop()
                stack.append(token)

            # 3) ')'라면 버리고 '(' 만날때까지 pop
            elif token == ')':
                while stack and token[-1] != '(':
                    result += stack.pop()
                # '('까지 버림
                stack.pop()

# 2. 피연산자는 그냥 result에 담기
        else:
            result += token

# 3. 혹시나 스택에 토큰이 남아있다면 모두 결과값에 담음
    while stack:
        result += stack.pop()

    print(f'#{tc} {result}')

