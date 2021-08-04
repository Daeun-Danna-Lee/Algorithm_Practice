import sys
input = sys.stdin.readline

n, k = map(int, input().split())
coins = [int(input()) for _ in range(n)]

count = 0

for coin in reversed(coins):
    if coin <= k:
        available_coin = k // coin
        k -= coin * (available_coin)
        count += available_coin

print(count)