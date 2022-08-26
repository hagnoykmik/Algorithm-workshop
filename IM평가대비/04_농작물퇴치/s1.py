import sys
sys.stdin = open('input.txt')

t = int(input())

for tc in range(1, t + 1):
    n = int(input())
    farm = [list(map(int, input().split())) for _ in range(n)]

    for k in range(n * 2):
        for i in range(n):
            for j in range(n):
                if i - j +