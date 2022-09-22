# 완전 이진 트리
def pre(n):
    if n <= size:
        print(tree[n])
        pre(2 * n)
        pre(2 * n + 1)

tree = [0, 'A', 'B', 'C', 'D', 'E', 'F']  # 완전 이진 트리
size = len(tree) - 1                      # 마지막 정점 번호

pre(1)  # 1번 부터 순회
pre(2)  # 2번(B) 부터 순회하면 D, E하고 끝