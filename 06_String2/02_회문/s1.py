import sys
sys.stdin = open('sample_input.txt', encoding="utf-8")

t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())
    word = [input() for _ in range(n)]
    result = []

# 1. 가로로 찾기
    for i in range(n): #0
        for j in range(n-m+1): #0
            if word[i][j:j+m] == word[i][j:j+m][::-1]: #word[0][10]
                result.append(word[i][j:j+m])

# 2. 세로로 찾기
    chars = ''  # 세로 글자들을 넣을 빈 문자열
    for k in range(n): #0
        chars = ''
        for l in range(n):
            chars += word[l][k]
        if chars == chars[::-1]:
            result.append(chars)
    print(*result)



