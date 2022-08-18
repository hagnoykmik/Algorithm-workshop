import sys
sys.stdin = open('sample_input.txt')

t = int(input())

for tc in range(1, t+1):
    word = input()              # ABCCB

    my_stack = []               # test case바뀔 때 초기화 해줘야하니까 위치 for문 안에 지정
# 1. 문자열 담을 스택 만들기
    for char in word:

        if not my_stack:        # 스택이 비어있으면 문자열을 넣어줘
            my_stack.append(char)

        else:                   # 스택이 비어있지 않으면 비교
            if my_stack[-1] == char:  # 제일 최근 값과 넣을값이 같으면 제거
                my_stack.pop()
            else:
                my_stack.append(char) # 아니라면 스택에 넣어준다
    print(f'#{tc}', len(my_stack))
