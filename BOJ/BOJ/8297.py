import sys
from collections import deque

input = sys.stdin.readline

def checkMaxPath(possible_mushrooms, curr_index):
    left_sum = sum(possible_mushrooms[:curr_index])
    right_sum = sum(possible_mushrooms[curr_index+1:])

    return -1 if left_sum > right_sum else 1

n, t = map(int, input().split())
mushrooms = list(map(int, input().split()))

available_mushrooms = mushrooms
available_mushrooms[0] = 0
result = 0

current_location = 0
location_log = deque([current_location])

for i in range(t):

    # 버섯 다시 자라게 만들기
    if len(location_log) >= 3:
        grown_mushroom_location =  location_log.popleft()
        available_mushrooms[grown_mushroom_location] = mushrooms[grown_mushroom_location]

    result += available_mushrooms[current_location]
    available_mushrooms[current_location] = 0

    current_location += checkMaxPath(available_mushrooms[current_location-(t-i):current_location+(t-i)], t-i)
    location_log.append(current_location)

print(result)
    