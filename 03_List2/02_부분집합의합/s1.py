import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
# 0. 입력값 받기
    arr = list(map(int, input().split()))

    n = len(arr)

# i = 이진수 전구 중 어느 위치 킬건지에 대한 정보
    for i in range(1<<n): #부분 집합의 개수만큼 반복(1024번 반복)
        pass
    print(i)
