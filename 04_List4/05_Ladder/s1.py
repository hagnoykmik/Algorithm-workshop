# 교수님 코드

     #좌,우,위
dx = [0, 0, -1]
dy = [-1, 1, 0]

for tc in range(10):
    t = int(input())
    ladder = [input().split() for _ in range(100)]
# 1. 마지막 줄에서 x 지점 찾기
# 99번째 줄에서 2를 찾아라
    for i, number in enumerate(ladder[-1]): #래더 격자의 마지막 행
        if number == 2:
            x, y = 99, i #행, 열
            break

# 2. 사다리 타고 올라가기
# 행이 0이 될때까지
    while x > 0:
        #모든 지점에서 좌, 우, 위 다 보기
        for i in range(3): #좌, 우, 위
            nx = x + dx[i]
            ny = y + dy[i]

            #범위 확인 & 다음에 갈 수 있는 곳(1)인가요
            if 0 <= nx <= 100 and 0 <= ny <= 100 and ladder[nx][ny] == 1:
                ladder[x][y] = '0' #이미 지나간 길은 0으로 바꿔줌
                #맞으면 갱신
                x, y = nx, ny

    print(f'#{tc} {y}') #열