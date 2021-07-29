import sys
input = sys.stdin.readline

N, K = map(int, input().split())
name_len = [len(input().rstrip()) for _ in range(N)] 
count = 0
data = [0] * 21

for i in range(N):
    if i > K:
        data[name_len[i-K-1]] -= 1
        print("i:{} \t name_len[i-K-1]: {} \t data[name_len[i-K-1]]: {}".format(i, name_len[i-K-1], data[name_len[i-K-1]]))
    print("prev >>> count: {} \t data[name_len[i]]: {} \t {}".format(count, data[name_len[i]], data))
    count += data[name_len[i]]
    data[name_len[i]] += 1
    print("after >>> count: {} \t data[name_len[i]]: {} \t {}".format(count, data[name_len[i]], data))

print(count)