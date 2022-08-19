def dfs(x, y):
    global total
    total += 1
    visited[x][y] = True

    # 델타 이동
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]

        if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny] and board[nx][ny] == 1:
            dfs(nx, ny)


# 0. 입력값 받기
n = int(input())
board = [list(map(int, input())) for _ in range(n)]  # 지도
visited = [[False] * n for _ in range(n)]  # 방문체크리스트
result = []  # 단지내의 집 개수들의 모임


# 델타탐색
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


# 1. 이차원 리스트를 행 순회
for i in range(n):
    for j in range(n):
        # 2. 1이고(집) 아직 방문하지 않았으면(not visited) DFS 시작
        if not visited[i][j] and board[i][j] == 1:
            total = 0 # 단지가 시작할 때 초기화 해주기 위해서
            dfs(i, j) # 좌표 기준
            result.append(total)

print(len(result))
for i in sorted(result):
    print(i)

#print(len(result), *sorted(result), sep='\n') # 공백대신 줄바꿈으로 구분