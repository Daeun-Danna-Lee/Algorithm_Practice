import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = list(map(int, input().split()))

permutations = sorted(permutations(nums, m))

for row in permutations:
    print(' '.join(map(str, row)))
