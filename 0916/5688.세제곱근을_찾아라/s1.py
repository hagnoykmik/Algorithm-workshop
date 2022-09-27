import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    result = -1

    # 1부터 자기자신까지
    for x in range(1, n + 1):
        if x * x * x > n:
            break
        if x * x * x == n:
            result = x
            break

    print(f'#{tc} {result}')