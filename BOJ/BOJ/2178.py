import sys
from collections import deque

input = sys.stdin.readline


def solve(index, x, y):
    global maze

    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    queue = deque()
    queue.append((index, x, y))
    maze[y][x] = 0

    while queue:
        index, x, y = queue.popleft()
        saved_index = index

        for i in range(4):
            index = saved_index
            next_x = x + dx[i]
            next_y = y + dy[i]

            if 0 <= next_x < m and 0 <= next_y < n:
                if maze[next_y][next_x] == 1:
                    index += 1
                    maze[next_y][next_x] = index
                    queue.append((index, next_x, next_y))

n, m = map(int, input().split())
maze = [list(map(int, list(input().rstrip()))) for _ in range(n)]

solve(1, 0, 0)

print(maze[n-1][m-1])