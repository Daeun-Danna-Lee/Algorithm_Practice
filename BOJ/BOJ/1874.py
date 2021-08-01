import sys
input = sys.stdin.readline

n = int(input())
input_list = [int(input()) for _ in range(n)]

list = []
pop_list = []
result = []

curr = 1

for i in range(n):
    while input_list[i] >= curr:
        result.append('+')
        list.append(curr)
        curr += 1
    
    if list[-1] == input_list[i]:
        result.append('-')
        pop_list.append(list.pop())

if pop_list == input_list:
    print(('\n').join(result))
else:
    print("NO")