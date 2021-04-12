import sys
import heapq

input = sys.stdin.readline

n, m = map(int, input().split())
cards = list(map(int, input().split()))

queue = []

for card in cards:
    heapq.heappush(queue, card)

for _ in range(m):
    x = heapq.heappop(queue)
    y = heapq.heappop(queue)
    heapq.heappush(queue, x + y)
    heapq.heappush(queue, x + y)

print(sum(queue))