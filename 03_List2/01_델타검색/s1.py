import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
# 0. 입력값 받기
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]

# 1. 상하좌우의 인덱스 값 담기
    direct_i = [-1, 0, 1, 0] #i에 더할 값
    direct_j = [0, 1, 0, -1] #j에 더할 값

    sum_d = 0 #절대값들의 합을 넣을 변수 생성

    for i in range(n):
        for j in range(n):
            for k in range(4): #4방향
                di = i + direct_i[k]
                dj = j + direct_j[k]

# 2. 인덱스 범위를 벗어났을 경우
                if di < 0 or di > 4 or dj < 0 or dj > 4:
                    continue

# 3. 상하좌우 값과의 차의 절대값 구하기
                difference = 0 #기준값과 4개의 차이의 합을 넣을 변수 생성

                difference = arr[i][j] - arr[di][dj]

                if difference < 0:
                    difference = difference * -1 #절대값
                else:
                    difference = difference * 1

# 4. 절대값의 합을 구하기
                sum_d += difference

# 5. 25개 요소의 총합을 구하기
    print(f'#{tc} {sum_d}')