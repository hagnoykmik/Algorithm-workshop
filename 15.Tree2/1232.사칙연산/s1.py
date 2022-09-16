import sys
sys.stdin = open('input.txt')

# 람다함수
cal = {
    '+': lambda x, y: x + y,
    '-': lambda x, y: x - y,
    '/': lambda x, y: x // y,
    '*': lambda x, y: x * y,
}

for tc in range(1, 11):
    n = int(input())
    tree = [0] * (n + 1)

    arrs = [list(map(lambda x : int(x) if x.isdigit() else x,input().split()))for _ in range(n)]

    for arr in arrs[::-1]:
        if len(arr) == 2:
            tree[arr[0]] = arr[1]
        else:
            tree[arr[0]] = cal[arr[1]](tree[[arr[2]]], tree[arr[3]])

    print(f'#{tc} {tree[1]}')




