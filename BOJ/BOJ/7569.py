from collections import deque

M, N, H = map(int, input().split())

tomato = []
queue = deque()
for z in range(H):
    tomato.append([])
    for i in range(N):
        tomato[z].append(list(map(int, input().split())))
        for j in range(M):
            if tomato[z][i][j] == 1:
                queue.append([z, i, j])

def bfs():
    while queue:
        curr_z, curr_x, curr_y = queue.popleft()

        dx = [0, 0, 1, -1, 0, 0]
        dy = [1, -1, 0, 0, 0, 0]
        dz = [0, 0, 0, 0, 1, -1]

        for i in range(6):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            new_z = curr_z + dz[i]

            if 0 <= new_x < N and 0 <= new_y < M and 0 <= new_z < H:
                if tomato[new_z][new_x][new_y] == 0:
                    tomato[new_z][new_x][new_y] = tomato[curr_z][curr_x][curr_y] + 1
                    queue.append([new_z, new_x, new_y])

if len(queue) == H * M * N:
    print(0)

else:
    can = True
    bfs()
    ans = 0
    for box in tomato:
        if not can:
            break
        for r in box: 
            if not can:
                break
            if 0 in r: 
                print(-1)
                can = False
                break
            ans = max(max(r), ans)
    if can:
        print(ans - 1) 