import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
# 0. 입력값 받기
    arr = list(map(int, input().split()))

    n = len(arr)

# 1. 모든 부분집합을 생성
    for i in range(1<<n): #부분 집합의 개수만큼 반복(1024번 반복)


# 2. 합을 구해야 한다