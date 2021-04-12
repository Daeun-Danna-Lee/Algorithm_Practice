import sys

input = sys.stdin.readline

m, n = map(int, input().split())

for i in range(m, n+1):
    cnt = 0
    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            cnt += 1
            break
    if cnt == 0 and i != 1:
        print(i)