import sys

input = sys.stdin.readline

givenString = input().rstrip()
bomb = list(input().rstrip())

stack = []

for char in givenString:
    stack.append(char)

    if char == bomb[-1]:
        if stack[-len(bomb):] == bomb:
            del stack[-len(bomb):]

if stack:
    print(*stack, sep='')
else:
    print("FRULA")