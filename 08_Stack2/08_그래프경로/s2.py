import sys
sys.stdin = open('sample_input.txt')

# 3. DFS 탐색
def dfs(v):
    visited[v] = True

    for next_v in graph[v]:
        if not visited[next_v]:
            dfs(next_v)


# 0. 입력값 받기
t = int(input())

for tc in range(1, t+1):
    V, E = map(int, input().split()) # 노드, 간선

    # 1. 인접 리스트 만들기
    graph = [[] for _ in range(V + 1)]

    for i in range(E):
        v1, v2 = map(int, input().split())
        graph[v1].append(v2)

    # 출발, 도착 노드
    S, G = map(int, input().split())

    # 2. 방문 처리 리스트 만들기
    visited = [False] * (V + 1)

    dfs(S)

    if visited[G]:
        print(f'#{tc} 1')
    else:
        print(f'#{tc} 0')

