from collections import deque

M, N = map(int, input().split())

tomato = []
queue = deque()
for i in range(N):
    tomato.append(list(map(int, input().split())))
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])

def bfs():
    while queue:
        curr_x, curr_y = queue.popleft()

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        for i in range(4):
            new_x = curr_x + dx[i]
            new_y = curr_y + dy[i]
            if 0 <= new_x < N and 0 <= new_y < M:
                if tomato[new_x][new_y] == 0:
                    tomato[new_x][new_y] = tomato[curr_x][curr_y] + 1
                    queue.append([new_x, new_y])

if len(queue) == M * N:
    print(0)

else:
    can = True
    bfs() # 익을 토마토는 다 익게 해요
    ans = 0
    for r in tomato: # 한 줄씩 검사합니다
        if 0 in r: # 안 익은 애가 있으면
            print(-1) # 이게 답이죠
            can = False
            break
        ans = max(max(r), ans) # 안 익은 애가 없다 👉🏻 가장 마지막날 날짜(?)를 답으로 가져야해요
    if can: # 모든 줄에 다행히 안 익은 토마토가 없었다면
        print(ans-1) # 가장 마지막날의 날짜 - 1 을 출력해주면 돼요