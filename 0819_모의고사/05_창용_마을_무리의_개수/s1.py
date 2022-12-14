import sys
sys.stdin = open('s_input.txt')


def dfs(r):
    visited[r] = True

    for next_r in graph[r]:
        if not visited[next_r]:
            dfs(next_r)


# 0. 입력값받기
t = int(input())

for tc in range(1, t+1):
    n, m = map(int, input().split())  # 사람 수, 관계 수
    total = 0                         # 무리의 수
    # 방문 처리 리스트
    visited = [False] * (n + 1)

    # 관계도
    graph = [[] for _ in range(n + 1)]

    for i in range(m):
        r1, r2 = map(int, input().split())
        graph[r1].append(r2)
        graph[r2].append(r1)

    for i in range(1, n+1):
        if not visited[i]:              # 아직안갔으면
            total += 1
            dfs(i)