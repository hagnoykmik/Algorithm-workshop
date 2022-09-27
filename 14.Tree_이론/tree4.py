# 정점의 개수
def preorder(n):
    global cnt
    if n:
        cnt += 1
        preorder(ch1[n])
        preorder(ch2[n])


# 마지막 정점의 번호
def preorder(n):
    global last_v
    if n:
        last_v = n  # 덮어쓰기 (더이상 순회할 게 없을 때까지)
        preorder(ch1[n])
        preorder(ch2[n])


# global cnt없이 순회한 정점 수를 리턴하는 함수
def f(n):
    # L + R + V
    if n == 0:  # 자식이 없으면(서브트리가 비어있으면)
        return 0
    else:
        L = f(ch1[n])
        R = f(ch2[n])
        return L + R + 1