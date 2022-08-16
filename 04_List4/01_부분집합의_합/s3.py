#교수님 코드
import sys
sys.stdin = open('../../03_List2/02_부분집합의합/input.txt')

t = int(input())

for tc in range(1, t+1):
    n, k = input().split()
    result = 0

# 1. 부분집합의 개수만큼 반복 (모든 부분집합 검색)
    for i in range(1, 1 << 12): #부분집합의 개수만큼 반복(공집합 포함 X)
        length, total = 0, 0  # n,k랑 비교

# 2. 몇 번째 원소를 선택할지 결정
        for j in range(12):
            if i & (1 << j):
                length += 1
                total += j + 1 #j는 인덱스라서 1이 작다

# 3. 조건을 만족하면(N개, 합이 K) 결과값 += 1
        if length == n and total == k:
            result += 1

    print(f'#{tc} {result}')

