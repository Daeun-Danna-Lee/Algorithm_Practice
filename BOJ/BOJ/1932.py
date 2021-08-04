import sys
input = sys.stdin.readline

t = int(input()) 
n=[list(map(int,input().split())) for _ in range(t)]  

for i in range(1,t): 
    for j in range(len(n[i])): 
        if j == 0: 
            n[i][j] += (n[i-1][j]) 
        elif j==i: 
            n[i][j] +=(n[i-1][j-1]) 
        else: 
            n[i][j] += (max(n[i-1][j],n[i-1][j-1])) 

print(max(n[t-1]))

