import sys
input = sys.stdin.readline

dict = {')': '(', ']': '['}

while True:
    string = input().rstrip()

    if string == '.':
        break

    stack = []
    isCorrect = True
    for char in string:
        if char == '(' or char == '[':
            stack.append(char)
        elif char == ')' or char == ']':
            if len(stack) == 0:
                isCorrect = False
                print("no")
                break
            else:
                if stack[-1] == dict[char]:
                    stack.pop()
                else:
                    isCorrect = False
                    print("no")
                    break

    if isCorrect:
        if len(stack) == 0:
            print("yes")
        else:
            print("no")