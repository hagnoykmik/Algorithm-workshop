# DFS

# 하 우

# 메모이제이션
import sys
sys.stdin = open()


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]
memo = [[0] * n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 1번. 원래 값을 넣어준다
        memo[i][j] += matrix[i][j]

        # 첫번째 값은 그냥 지나간다
        if i == 0 and j == 0:
            continue

        # 2번. 위, 왼쪽을 더해서 최고값으로 갱신
        if i == 0:     # 0번째 행
            memo[i][j] += memo[i][j - 1]
        elif j == 0:   # 0번 째 열
            memo[i][j] += memo[i - 1][j]
        else:          # 왼쪽이랑 위쪽 중에서 더 작은 값을 더한다
            memo[i][j] += min(memo[i][j - 1], memo[i - 1][j])

print(f'#{tc} {memo[n - 1][n - 1]}')