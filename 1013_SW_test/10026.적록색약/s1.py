# 일반인
import sys
sys.stdin = open('input.txt')

def search(x, y, color):
    visited[x][y] = True

    if color == 'G':
        area[x][y] = 'R'

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < n and area[nx][ny] == color:
            search(nx, ny, color)
            visited[x][y] = False


# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


n = int(input())
area = [list(input()) for _ in range(n)]
visited = [[False] * n for _ in range(n)]
cnt_public = 0
cnt_red_green = 0

for x in range(n):
    for y in range(n):
        if visited[x][y]:
            continue
        else:
            color = area[x][y]
            search(x, y, color)
            cnt_public += 1

print(area)
print(cnt_public, cnt_red_green)
