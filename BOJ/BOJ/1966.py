import sys
from collections import deque 
input = sys.stdin.readline

tc = int(input())

for _ in range(tc):
    n, m = map(int, input().split())
    queue = deque(map(int, input().split()))

    count = 1
    while True:
        if m == 0:
            if max(queue) == queue[m]:
                print(count)
                break
            else:
                m = len(queue) - 1
                queue.append(queue.popleft())
        else:
            m -= 1
            if max(queue) == queue[0]:
                count += 1
                queue.popleft()
            else:
                queue.append(queue.popleft())