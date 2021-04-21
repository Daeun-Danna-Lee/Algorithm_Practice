import sys
from itertools import combinations

input = sys.stdin.readline

vowels = ['a', 'e', 'i', 'o', 'u']

l, c = map(int, input().split())
words = sorted(input().split())

print(words)

for pw in combinations(words, l):
    char_cnt = 0
    for char in pw:
        if char in vowels:
            char_cnt += 1
    if char_cnt >= 1 and len(words) - 2:
        print(''.join(pw)) # 조합된 걸 문자열로 변환