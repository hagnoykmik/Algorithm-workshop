import sys
sys.stdin = open('sample_input.txt')

'''
start 위치가 이동할 때마다 바뀐다
방문 했던 곳 또 가도 됨
모든 경우의 수 구하고 마지막에 중복 제거
'''

t = int(input())
board = [list(input().split()) for _ in range(4)]
visited = [[0] * 4 for _ in range(4)]

# 이동범위 - 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


for x in range(4):
     for y in range(4):
        # start
        num = ''  # 7자리 숫자를 담는다

        i = 0

        # 7 자리가 될 때까지 담는다
        while len(num) < 7:

            num += board[x][y]
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < 4 and 0 <= ny < 4:
                x, y = nx, ny
            else:
                i = (i + 1) % 4
                x += dx[i]
                y += dy[i]

        print(num)














