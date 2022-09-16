import sys
sys.stdin = open('input.txt')

from itertools import combinations

t = int(input())
for tc in range(1, t + 1):
    n, b = map(int, input().split())
    hi = list(map(int, input().split()))
    subset = []
    top = 0
    sum_list = []

    for i in range(1, len(hi)+1):
        # i개로 이루어진 부분집합 구하기
        subset = list(combinations(hi, i))
        for h in subset:
            # 부분 집합의 합
            s = sum(h)
            if s >= b:
                sum_list.append(s)

    # 부분 집합의 합이 b이상인 것 중에 최솟값과 b의 차이
    result = min(sum_list) - b

    print(f'#{tc} {result}')