import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    n = int(input())
    h = list(map(int, input().split()))
    result = 0

    for i in range(n - 5 + 1):     # 건물 5개씩 비교
        arr = []                   # i가 바뀔 때(5개 비교 후) 초기화
        max_h = 0                  # 기준 건물과 비교할 건물 중 가장 높은 건물
        for j in range(i, i + 5):  # 비교할 건물의 높이 담기
            arr.append(h[j])

        s = arr[2]             # 중간값이 비교 기준

        # 5개의 건물 중 기준건물이 제일 클 때
        if s > arr[0] and s > arr[1] and s > arr[3] and s > arr[4]:
            # 나머지 4건물 중 가장 큰 건물과 비교
            if arr[0] > max_h:
                max_h = arr[0]
            if arr[1] > max_h:
                max_h = arr[1]
            if arr[3] > max_h:
                max_h = arr[3]
            if arr[4] > max_h:
                max_h = arr[4]

            result += s - max_h

    print(f'#{tc} {result}')

