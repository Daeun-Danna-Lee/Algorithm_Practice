import sys
from math import factorial

input = sys.stdin.readline

a, b = map(int, input().split())

print((factorial(a) // (factorial(b) * factorial(a-b))))