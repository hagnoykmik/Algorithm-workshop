import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
# 0. 입력값 받기
    k, n, m = map(int, input().split())
    idx = list(map(int, input().split())) #충전기가 있는 정류소 위치를 나타내기 위해 인덱스로 사용
    # print(k, n, m, arr)

# 1. 정류소 위치를 나타낼 새로운 배열 만들기
    arr = [0] * (n + 1)
    for i in range(m):
        arr[idx[i]] = 1 #충전기가 있는 정류소는(idx리스트에 있는 숫자=정류소 넘버) 값을 1로 바꿔주기
    # [0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0]

# 2. 충전할 곳 정하기

    cnt = 0 #충전 횟수
    s = 0 #start위치는 idx = 0
    while s + k < n:
        for j in range(s, s + k + 1): #1번 충전으로 갈 수 있는 거리 범위 내에서
            if arr[j] == 1:
                cnt += 1
                s = j




