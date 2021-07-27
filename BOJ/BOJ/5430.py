import sys
from collections import deque

input = sys.stdin.readline

def processArray(arrayStr):
    newArrayStr = arrayStr[1:-2] # 문자열에서 [] 제거
    arrayResult = deque(newArrayStr.split(','))

    if arrayResult[0] == '':
        arrayResult = []

    return arrayResult

def printArray(array):
    print('[', end='')
    print(','.join(array), end='')
    print(']')


# main
T = int(input())

for _ in range (T):
    reverseCnt = 0
    errorThrown = False

    p = input()
    n = int(input())
    arrayStr = input()
    array = processArray(arrayStr) # 처리가 끝난 배열

    for command in p:
        if command == 'R':
            reverseCnt += 1
        elif command == 'D':
            if len(array) == 0:
                print("error")
                errorThrown = True
                break
            if reverseCnt % 2 == 0:
                array.popleft()
            else:
                array.pop()

    if reverseCnt % 2 == 1:
        array.reverse()

    if not errorThrown:
        printArray(array)
