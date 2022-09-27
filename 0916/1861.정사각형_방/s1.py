import sys
sys.stdin = open('input.txt')


# 상, 하, 좌, 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    rooms = [list(map(int, input().split())) for _ in range(n)]
    k = {}

    # 모든 방에서 다 해봐야한다.
    for x in range(n):
        for y in range(n):
            cnt = 1
            start = rooms[x][y]
            while True:
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]

                    # 이동 범위고 정확히 1크면 이동
                    if 0 <= nx < n and 0 <= ny < n and rooms[nx][ny] - rooms[x][y] == 1:
                        cnt += 1
                        x, y = nx, ny
                        break

                # 모든 방향을 다 돌았는데 못간다면
                else:
                    k[start] = cnt
                    break

    # print(k)
    # 최대 방 갯수
    max_cnt = max(k.values())
    max_list = [room for room, value in k.items() if max(k.values()) == value]
    # [38, 46, 54, 6, 14, 22, 30]

    print(f'#{tc} {min(max_list)} {max_cnt}')





