n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
x, y = 0, 0
d = 0

# 델타값(우->하->좌->상)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

for i in range(n * m, 0, -1):
    arr[x][y] = i

    nx = x + dx[d]
    ny = y + dy[d]

    # 범위 벗어나고 값이 없으면(0) 방향바꾸기
    if 0 <= nx < n and 0 <= ny < m and arr[nx][ny] == 0:
        x += dx[d]
        y += dy[d]
    else:
        d = (d + 1) % 4
        x = x + dx[d]
        y = y + dy[d]

for k in arr:
    print(*k)

