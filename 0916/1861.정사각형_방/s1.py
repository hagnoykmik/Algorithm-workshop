import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]

    print(n)