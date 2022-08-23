# 윤지코드

import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))
    result = 0

    for i in range(2, n-2):  # 기준빌딩범위
        max_num = 0
        for j in range(i-2, i+3):  # 다섯개 비교
            if j == i:  # 자기자신이면
                continue
            if max_num < h[j]:
                max_num = h[j]

    if max_num < h[i]:  # 기준값과 비교했을 때 작아야함
            result += h[i] - max_num

    print(f'#{tc} {result}')

