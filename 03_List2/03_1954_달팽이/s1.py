import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr = [[0 for _ in range(n)] for _ in range(n)] #초기 nxn배열 생성
    print(arr)

    for i in range(n):
        for j in range(n):
            pass
