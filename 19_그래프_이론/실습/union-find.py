import sys
sys.stdin = open('input.txt')

# # 2. 재귀
# def find_set(node):
#     if node != parent[node]:
#         return find_set(parent[node])
#     return node


# # 1. 반복문
# def find_set(node):
#     # 내가 부모이면 멈춘다 => root node => 집합의 대표값
#     while node != parent[node]:
#         # node에 대표값을 넣어서 다시 찾아보자
#         node = parent[node]
#     return node


# 3. 재귀 - 경로 압축(부모 노드를 대표값으로 만듦) !중요!
def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]   # 루트를 반환하면서 자식 값을 다 루트노드로 바꿔준다(경로 압축)


n, m = 6, 4                       # 정점, 간선(Union 횟수) 개수
parent = list(range(n + 1))       # Make-set (자기 자신을 가리키는 집합 n개)

for _ in range(m):
    x, y = map(int, input().split())           # union을 할 대상 (# 1, 3)(# 2, 3)
    x_root, y_root = find_set(x), find_set(y)  # Find (같은 집합인지 확인)
    # (# 1, 3), (# 2, 1)

    # Union (루트가 다르면 합칠거야 = 부모 노드의 걔를 끌어다 쓸게)
    if x_root != y_root:  # 서로소 집합인 경우만 합집합 연산
        # 그냥 작은 수에 붙이겠다 (3의 대표값을 1로 한다)(2의 대표값도 1)
        if x_root < y_root:
            parent[y_root] = x_root
        else:
            parent[x_root] = y_root


# 출력
for i in range(1, n + 1):
    print(find_set(i), end=' ')

print()
print(parent)