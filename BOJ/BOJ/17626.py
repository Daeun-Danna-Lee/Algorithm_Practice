import sys

input = sys.stdin.readline

squares = [0, 1, 4, 9, 16, 25]

n = int(input())

curr_num = 0
curr_square = 0

# DP를 위한 리스트를 만드는 로직
if n > 25:
    curr_num = 5
    curr_square = 25
    while True:
        curr_num += 1
        curr_square = curr_num ** 2

        if curr_square > n:
            break

        squares.append(curr_square)

        
count = 0
for i in range(len(squares)-1, 0, -1):
    if squares[i] > n:
        del squares[i]
    else:
        print("squares[{}]: {}".format(i, squares[i]))
        count += 1
        n -= squares[i]
        print("current n:", n)

if n == 1:
    count += 1

print(count)