import sys
sys.stdin = open('1in.txt')


t = 10

for tc in range(1, t+1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]
    # 상하좌우
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    # 절대값의 누적합
    sum_l = 0


# 절대값 구하기(누적합)
    for x in range(n):
        for y in range(n):
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]

                # 범위 설정
                if 0 > nx or nx > n or 0 > ny or ny > n:
                    continue

                # 절댓값 구하기
                d = 0

                d = board[nx][ny] - board[x][y]

                if d < 0:
                    d = d * -1
                else:
                    d = d * 1

                sum_l += d

    print(f'#{tc} {sum_l}')

