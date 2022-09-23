import sys
sys.stdin = open('sample_input.txt')

'''
start 위치가 이동할 때마다 바뀐다(재귀함수 이용)
특이사항 : 방문 했던 곳 또 가도 됨
모든 경우의 수 구하고 마지막에 중복 제거
'''


def search(x, y):
    global num
    print(len(num))
    # 이동을 다 했으면 출력
    if len(num) == 7:
        result.add(num)
        return

    # 아니면 숫자 담으러 이동
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < 4 and 0 <= ny < 4:
            num += board[x][y]
            search(nx, ny)
            num = num[:-1]


# 이동범위 - 동서남북
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

t = int(input())
for tc in range(1, t + 1):
    board = [list(input().split()) for _ in range(4)]

    num = ''   # 7자리 숫자를 담는다
    result = set()

    for x in range(4):
        for y in range(4):
            num += board[x][y]
            search(x, y)

    print(f'#{tc} {len(result)}')












