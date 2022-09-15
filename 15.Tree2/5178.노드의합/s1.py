import sys
sys.stdin = open('sample_input.txt')

t = int(input())
for tc in range(1, 11):

    def traverse(v):
        if v <= n:
            visit(n)
            traverse(v * 2)
            traverse(v * 2 + 1)

    n, m, l = map(int, input().split())

    left = [0] * (n + 1)
    right = [0] * (n + 1)

    for i in range(m):
        c, v = map(int, input().split())

        p = c // 2

        if left[p] == 0:
            left[p] = c
        else:
            right[p] = c

    traverse(1)