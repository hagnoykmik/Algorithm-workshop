import sys

sys.stdin = open('sample_input.txt')

t = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, t + 1):
    n, k = input().split()
    n = int(n)
    k = int(k)
    m = len(arr)  # 원소의 개수
    result = 0

    # 부분집합의 개수만큼 반복 & 모든 부분집합 검색
    for i in range(1 << m):
        cnt = 0  # 부분집합의 원소가 n개임을 확인하기 위함
        sum_s = 0  # n개의 원소들의 합

        for j in range(m):  # j = 0부터 m-1까지 인덱스로 이용(arr의 값)
            if i & (1 << j):  # i의 j번째 비트가 i이면(부분집합에 포함되면)
                cnt += 1  # 넣을때마다 count함
                sum_s += j + 1

        if cnt == n and sum_s == k: # 원소가 n개가 되면
            result += 1

    print(f'#{tc} {result}')