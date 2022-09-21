import sys
sys.stdin = open('input.txt')

# 연산을 위한 람다함수
cal = {
    '+': (lambda x, y: x + y),
    '-': (lambda x, y: x - y),
    '*': (lambda x, y: x * y),
    '/': (lambda x, y: x // y),
}


for tc in range(1, 11):
    n = int(input())

    # 숫자라면 정수로 받고 아니면 문자열로 받는다.
    arrs = [list(map(lambda x: int(x) if x.isdigit() else x, input().split())) for _ in range(n)]
    nods = [0] * (n + 1)

    # 숫자를 채워야 연산이 가능하니까 거꾸로 담는다.
    for arr in arrs[::-1]:
        # 리프 노드라면
        if len(arr) == 2:
            nods[arr[0]] = arr[1]
        # 값이 연산자라면
        else:
            nods[arr[0]] = cal[arr[1]](nods[arr[2]], nods[arr[3]])

    print(f'#{tc} {nods[1]}')