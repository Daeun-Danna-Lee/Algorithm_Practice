import sys
from itertools import combinations

input = sys.stdin.readline

n, m = map(int, input().split())

combinations = combinations(range(1, n+1), m)

for row in combinations:
    print(' '.join(map(str, row)))
