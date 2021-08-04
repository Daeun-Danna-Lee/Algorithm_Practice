import sys
from itertools import permutations

input = sys.stdin.readline

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

permutations = sorted(set(permutations(nums, m)))

for row in permutations:
    print(' '.join(map(str, row)))