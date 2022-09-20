import sys
sys.stdin = open('sample_input.txt')


# 중위순회(L < V < R)
def inorder(v):
    global num
    if v <= n:
        inorder(v * 2)
        tree[v] = num
        num += 1
        inorder(v * 2 + 1)


t = int(input())
for tc in range(1, t + 1):
    n = int(input())

    tree = [0] * (n + 1)
    num = 1     # 1부터 n까지로 채운다

    inorder(1)

    print(f'#{tc} {tree[1]} {tree[n // 2]}')