import sys
sys.stdin = open('input.txt')

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    board = [list(map(int, input().split())) for _ in range(n)]

