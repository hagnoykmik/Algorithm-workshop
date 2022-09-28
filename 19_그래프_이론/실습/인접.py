'''
마지막 정점 번호 6 (0번부터 시작)
간선 8개
6 8
0 1 0 2 0 5 0 6 4 3 5 3 6 4 5 4
'''

v, e = map(int, input().split())
arr = list(map(int, input().split()))

graph = [[0] * (v + 1) for _ in range(v + 1)]  # 인접 행렬
adjlist = [[] for _ in range(v + 1)]           # 인접 리스트

for i in range(e):
    n1, n2 = arr[i * 2], arr[i * 2 + 1]

    # 행렬
    graph[n1][n2] = 1
    graph[n2][n1] = 1   # 방향이 없는 경우에만

    # 리스트
    adjlist[n1].append(n2)
    adjlist[n2].append(n1)

print(graph)
print(adjlist)

