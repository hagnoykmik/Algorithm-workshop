import sys
sys.stdin = open('sample_input.txt')


# 최소힙
def tree(v):

    c = v
    p = c // 2

    # 부모가 있거나, 부모 > 자식이면 자리 교환
    while p and nods[p] > nods[c]:
        nods[p], nods[c] = nods[c], nods[p]

        c = p
        p = c // 2


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    nods = list(map(int, input().split()))
    result = 0

    for i in range(n):
        tree(i)

    # i > 0 인 경우
    while n:
        n //= 2
        result += nods[n]

    print(f'#{tc} {result}')
