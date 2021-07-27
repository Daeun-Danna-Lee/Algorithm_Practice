import sys

input = sys.stdin.readline

givenString = input().rstrip()
bomb = input().rstrip()

while True:
    newString =  givenString.replace(bomb, '')

    if len(newString) == 0:
        print("FRULA")
        break
    
    if givenString == newString:
        print(givenString)
        break
    else:
        givenString = newString