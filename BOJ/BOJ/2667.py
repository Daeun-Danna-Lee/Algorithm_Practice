import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

def bfs(x, y, index):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((x, y))
    houses[x][y] = index

    while queue:
        x, y = queue.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx >= 0 and nx < n and ny >= 0 and ny < n:
                if houses[nx][ny] == 1:
                    queue.append((nx, ny))
                    houses[nx][ny] = index
                    count[index] += 1

houses = [[0] for _ in range(n)]

for i in range(n):
    row = list(input().rstrip())
    houses[i] = list(map(int, row))

count = [0, 0]
for i in range(n):
    index = 1
    for x in range(n):
        for y in range(n):
            if houses[x][y] == 1:
                count.append(1)
                index += 1
                bfs(x, y, index)

print(len(count[2:]))
print(('\n').join(map(str, sorted(count[2:]))))
