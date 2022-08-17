import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())

    # 메모이제이션
    def fibo(n):
        if memo[n-1][n] == - 1:                        # 계산된 적이 없다면
            memo[n] = fibo(n - 1) + fibo(n - 2)
        return memo[n]


    memo = [[-1] * 101]                             # 인덱스를 100까지 만들어준다
    memo[0] = 1
    memo[-1] = 1

    for i in range(100):
        print(fibo(i))