import sys
sys.stdin = open('sample_input.txt')


# 최소힙
def tree(v):
    global last
    last += 1       # 마지막 정점 추가
    heap[last] = v  # 마지막 정점에 키 값을 넣는다

    c = last
    p = c // 2

    # 부모가 있거나, 부모 > 자식이면 자리 교환
    while p and heap[p] > heap[c]:
        heap[p], heap[c] = heap[c], heap[p]

        c = p
        p = c // 2


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    nods = list(map(int, input().split()))

    heap = [0] * (n + 1)
    last = 0
    result = 0

    for i in nods:
        tree(i)

    # i > 0 인 경우
    while n:
        n //= 2
        result += heap[n]

    print(f'#{tc} {result}')
