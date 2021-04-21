import sys

input = sys.stdin.readline

dwarf = []

for i in range(9):
    dwarf.append(int(input()))

dwarf.sort()

for i in range(8):
    for j in range(i+1, 9):
        if sum(dwarf) - dwarf[i] - dwarf[j] == 100:
            for k in range(9):
                if k != i and k != j:
                    print(dwarf[k])
            quit()