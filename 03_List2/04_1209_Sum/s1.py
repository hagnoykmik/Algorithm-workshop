import sys
sys.stdin = open('input.txt')

t = 10
for tc in range(1, t+1):
# 0. 입력값 받기
    n = input()
    arr = [list(map(int, input().split())) for _ in range(100)]

# 초기 max값 설정
    maxS = float('-inf')  # 합의 최대값을 담을 변수

# 1. 행의 합 구하기 + max값 갱신
    for i in range(100):
        rs = 0  # 행의 합 (한줄돌면(새로운 i로 되면) 리셋)
        for j in range(100):
            rs += arr[i][j]

            if maxS < rs:
                maxS = rs

# 2. 열의 합 구하기 + max값 갱신
    for i in range(100):
        cs = 0  # 열의 합
        for j in range(100):
            cs += arr[j][i]

            if maxS < cs:
                maxS = cs

# 3. (↘) 대각선 합 구하기 + max값 갱신
    s1 = 0  # 우측으로 내려가는 대각선
    for i in range(100):
        s1 += arr[i][i]

        if maxS < s1:
            maxS = s1

# 4. (↙) 대각선 합 구하기
    s2 = 0
    for i in range(100):
        s2 += arr[i][99 - i]

        if maxS < s2:
            maxS = s2

# 5. 결과값 출력
    print(f'#{tc} {maxS}')