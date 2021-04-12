import sys


input = sys.stdin.readline

m, n = map(int, input().split())
primes = []

for i in range(m, n+1):
    cnt = 0
    for j in range(2, i):
        if i % j == 0:
            cnt += 1
    if cnt == 0:
        primes.append(i)
        print(i)