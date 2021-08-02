import sys
input = sys.stdin.readline

pw_dict = {}
n, m = map(int, input().split())

for _ in range(n):
    site, pw = map(str, input().rstrip().split())
    pw_dict[site] = pw

for _ in range(m):
    print(pw_dict[input().rstrip()])