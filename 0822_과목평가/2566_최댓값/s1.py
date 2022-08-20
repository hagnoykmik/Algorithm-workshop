# 행 우선 순회

# 0. 입력값 받기
n = [list(map(int, input().split())) for _ in range(9)]  # 인덱스는 그냥 0부터 8로 지정됨

# 1. 행 우선 순회로 조회하면서 최댓값 담기

max_n = 0        # 최댓값
row, col = 0, 0  # 최댓값의 인덱스(행, 열)

for r in range(9):
    for c in range(9):
        if max_n <= n[r][c]:
            max_n = n[r][c]
            row = r
            col = c

print(max_n)
print(row + 1, col + 1)  # 그래서 프린트할 때 +1 해준다
