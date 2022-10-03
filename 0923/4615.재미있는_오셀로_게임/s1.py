import sys
sys.stdin = open('sample_input(1).txt')


def search(x, y, i, player):
    # 종료 조건 (놓을 돌과 같은 색이면 리스트에 넣고 종료)
    # [1, 2, 1, 2, 놓을돌1] 일 경우 -> 정답 : [1, 2, 1, 1, 1] / 오답 : [1, 1, 1, 1, 1]
    if board[x][y] == player:
        check.append((board[x][y], x, y))
        return

    # 다른 색이면 리스트에 넣고 이동
    check.append((board[x][y], x, y))
    nx = x + dx[i]
    ny = y + dy[i]

    # 이동 가능하고 비어있으면 이동
    if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0:
        search(nx, ny, i, player)


# ↖, 상, ↗, 우, ↘, 하, ↙, 좌
dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [-1, 0, 1, 1, 1, 0, -1, -1]


t = int(input())
for tc in range(1, t + 1):
    n, m = map(int, input().split())

    # 게임판 초기 세팅 (가운데)
    board = [[0] * n for _ in range(n)]
    board[n // 2 - 1][n // 2 - 1] = 2
    board[n // 2 - 1][n // 2] = 1
    board[n // 2][n // 2 - 1] = 1
    board[n // 2][n // 2] = 2


    # 게임 시작
    for _ in range(m):
        y, x, player = map(int, input().split())

        # 인덱스에 맞추기 위해 -1을 해줌
        x, y = x - 1, y - 1            # 인덱스에 맞춰준다

        # 방향 탐색
        for i in range(8):
            check = [(player, x, y)]   # 리스트에 돌의 색과 (x, y) 좌표를 넣어준다 (색을 바꿔줄 때 이용)

            nx = x + dx[i]
            ny = y + dy[i]

            # 이동 가능하고 비어져 있으면 탐색 시작
            if 0 <= nx < n and 0 <= ny < n and board[nx][ny] != 0:
                search(nx, ny, i, player)

                # 검사 (2개 이상 들어있고 처음과 마지막이 같은색으로 되어있으면 색을 바꿔준다)
                if len(check) > 2 and check[0][0] == player and check[-1][0] == player:

                    # 색깔 바꿔주기
                    board[x][y] = player                  # 돌 놓기
                    # [(색깔, x좌표, y좌표) (1, 1, 1), (2, 1, 2), (1, 0, 1)]
                    for j in range(1, len(check) - 1):    # 사이에 낀 돌들 색 바꿔주기
                        board[check[j][1]][check[j][2]] = player

    # 게임 종료 시 남아있는 돌의 개수
    white, black = 0, 0
    for p in range(n):
        for q in range(n):
            if board[p][q] == 1:
                black += 1
            elif board[p][q] == 2:
                white += 1

    print(f'#{tc} {black} {white}')









