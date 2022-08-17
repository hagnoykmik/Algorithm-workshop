import sys
sys.stdin = open('sample_input.txt', encoding="utf-8")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    row = [input() for _ in range(n)]
    col = [' '] *n
# 0 . 세로로 읽기위해 문자열 다시 담아주기
    for i in range(n):
        for j in range(n):
            col[i] += row[j][i]

# 1. 가로, 세로로 찾기
    for i in range(n):
        for j in range(n-m+1):
            if row[i][j:j+m] == row[i][j:j+m][::-1]:
                word = row[i][j:j+m]
                print(word)
            else:
                word = col[i][j:j+m]
                print(word)