import sys
from collections import deque

input = sys.stdin.readline

tc = int(input())

def bfs(x, y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque((x, y))

    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx >= 0 and nx < n and ny >= 0 and ny < m:
                if field[nx][ny] == 1:
                    queue.append((nx, ny))
                    field[nx][ny] = 2

for i in range(tc):
    m, n, k = map(int, input().split())

    field = [[0]*m for _ in range(n)]

    for i in range(k):
        a, b = map(int, input().split())
        field[b][a] = 1

    count = 0

    for i in range(n):
        for j in range(m):
            if field[i][j] == 1:
                bfs(i, j)
                count += 1
    
    print(count)