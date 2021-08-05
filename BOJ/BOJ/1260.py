import sys
from collections import deque

input = sys.stdin.readline

def bfs(v):
    queue = deque()
    queue.append(v)

    visit_list_bfs[v] = 1

    while queue:
        v = queue.popleft()
        print(v, end=" ")

        for i in range(1, n+1):
            if visit_list_bfs[i] == 0 and graph[v][i] == 1:
                queue.append(i)
                visit_list_bfs[i] = 1

def dfs(v):
    visit_list_dfs[v] = 1
    print(v, end=" ")

    for i in range(1, n+1):
        if visit_list_dfs[i] == 0 and graph[v][i] == 1:
            dfs(i)

n, m, v = map(int, input().split())

graph = [[0]*(n+1) for _ in range(n+1)]
visit_list_bfs = [0] * (n + 1)
visit_list_dfs = [0] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1

dfs(v)
print()
bfs(v)
