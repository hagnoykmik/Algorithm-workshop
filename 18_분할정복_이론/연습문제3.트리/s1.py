import sys
sys.stdin = open('input.txt')

# 전위 순회
def preorder(v):
    if v:
        result_pre.append(v)
        preorder(ch1[v])
        preorder(ch2[v])

# 중위 순회
def inorder(v):
    if v != 0:
        inorder(ch1[v])
        result_in.append(v)
        inorder(ch2[v])

# 후위 순회
def postorder(v):
    if v:
        postorder(ch1[v])
        postorder(ch2[v])
        result_post.append(v)


t = 1
for tc in range(1, t + 1):
    n, v = map(int, input().split())
    tree = list(map(int, input().split()))

    # 부모 노드를 인덱스로 자식 노드 담기
    ch1 = [0] * (n + 1)
    ch2 = [0] * (n + 1)

    # 순회한 결과값을 담을 리스트
    result_pre = []
    result_in = []
    result_post = []


    for i in range(v):
        p, c = tree[2 * i], tree[2 * i + 1]

        if ch1[p] == 0:
            ch1[p] = c
        else:
            ch2[p] = c

    preorder(1)
    print('전위 순회 :', *result_pre)
    inorder(1)
    print('중위 순회 :', *result_in)
    postorder(1)
    print('후위 순회 :', *result_post)