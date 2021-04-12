import sys


input = sys.stdin.readline

eq = input()

if (int(eq[0]) + int(eq[4])) == int(eq[8]):
    print("YES")
else:
    print("NO")