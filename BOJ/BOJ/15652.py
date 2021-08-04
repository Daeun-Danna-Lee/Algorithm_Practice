import sys
from itertools import combinations_with_replacement

input = sys.stdin.readline

n, m = map(int, input().split())

combinations = combinations_with_replacement(range(1, n+1), m)

for row in combinations:
    print(' '.join(map(str, row)))
