# 교수님 코드

'''
E C B D가 집합이기만 하면 된다
3
3
0 1 0
1 0 1
0 1 0
1 2 3
'''


def find_set(node):
    if node != parent[node]:
        parent[node] = find_set(parent[node])
    return parent[node]


def union_set(x, y):
    if x != y:
        if x < y:
            parent[y] = x
        else:
            parent[x] = y


# 입력값 받기
n = int(input())
m = int(input())
parent = list(range(n+1))

# 유니온-파인드(길 연결하기)
for i in range(n):
    line = input().split()
    for j in range(n):
        if line[j] == '1':
            i_root, j_root = find_set(i + 1), find_set(j + 1)
            union_set(i_root, j_root)

# 여행계획 입력값
plans = list(map(int, input().split()))
root = find_set(plans[0])
result = 'YES'

print(parent)
# 여행 갈 수 있니~?
for i in range(1, m):
    if root != find_set(plans[i]):
        result = 'NO'
        break

print(result)