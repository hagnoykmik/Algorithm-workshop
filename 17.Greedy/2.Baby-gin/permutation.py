import sys
sys.stdin = open('input.txt')


# 완전 탐색(순열)
def f(i, k):
    if i == k:     # 다 채워졌으면 프린트
        print(p)
    else:
        for j in range(k):      # 모든 원소에 대해
            if used[j] == 0:    # 사용하지 않았다면
                p[i] = arr[j]   # p값을 채운다
                used[j] = 1     # 사용함으로 바꿈
                f(i + 1, k)
                used[j] = 0     # 다른 자리에서 사용하기 위해 초기화


t = int(input())
for tc in range(1, t + 1):
    arr = list(map(int, input()))
    n = len(arr)
    used = [0] * n  # 사용여부 확인
    p = [0] * n

    f(0, n)

    # triplet 검사
    while