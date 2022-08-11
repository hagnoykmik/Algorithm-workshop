import sys
sys.stdin = open('input.txt')

# 이 문제의 key point : 범위를 벗어나거나 값이 있으면 방향(인덱스)을 바꾼다

# 1. 델타값 정의
dx = [0, 1, 0 -1]
dy = [1, 0, -1, 0]
           # 우하좌상

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    snail = [[0] * n for _ in range(n)] #2차원 배열 초기화

    x, y = 0, 0 #출발 위치
    direction = 0 #처음 출발 방향이 오른쪽(인덱스)

# 2. 9번 반복
    for i in range(1, n*n +1): #1부터 9까지
        snail[x][y] = i
        # 오른쪽으로 이동
        nx = x + dx[direction]
        ny = y + dy[direction]

# 3. 범위안에 있는지 + 값이 없는지(0인지)
        if 0 <= nx < n and 0 <= ny < n and snail[nx][ny] == 0:
            x, y = nx, ny
        else: #방향을 바꿔서 다시 이동하자
            direction = (direction + 1) % 4 #0123(인덱스)을 반복하기 위해 나머지를 이용
            x += dx[direction]
            y += dy[direction]

    print(f'#{tc}')
    # 출력방법(1) 언패킹해서 숫자만 출력
    # for line in snail:
    #     print(*line)

    # 출력방법(2)
    for i in range(n):
        for j in range(n):
            print(snail, end=' ')