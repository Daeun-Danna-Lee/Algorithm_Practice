import sys
from itertools import combinations

input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
words = sorted(input().split())

answer = []
for pw in combinations(words, l):
    vowel_cnt = 0
    for char in pw:
        if char in vowels:
            vowel_cnt += 1
    if vowel_cnt >= 1 and vowel_cnt <= l - 2:
        print(''.join(pw))
