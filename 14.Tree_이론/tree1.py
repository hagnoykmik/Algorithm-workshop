'''
정점 번호 V : 1 ~ (E+1)
간선 수
부모-자식 순
E = 4
1 2 1 3 3 4 3 5
'''


# 전위순회 (root 먼저)
def preorder(n):
    if n:                  # 0이 아니면
        print(n)           # visit(n)
        preorder(ch1[n])   # left
        preorder(ch2[n])   # right


# 중위순회
def inorder(n):
    if n:
        inorder(ch1[n])
        print(n)
        inorder(ch2[n])


# 후위순위
def postorder(n):
    if n:
        postorder(ch1[n])
        postorder(ch2[n])
        print(n)


E = int(input())
V = E + 1
arr = list(map(int, input().split()))
root = 1

# 부모를 인덱스로 자식 번호 저장
ch1 = [0] * (V + 1)
ch2 = [0] * (V + 1)

for i in range(E):    # 2개씩 자르기
    p, c = arr[i * 2], arr[i * 2 + 1]
    if ch1[p] == 0:   # 아직 자식이 없으면
        ch1[p] = c    # 자식 1로 저장
    else:
        ch2[p] = c

# 순회
preorder(root)
