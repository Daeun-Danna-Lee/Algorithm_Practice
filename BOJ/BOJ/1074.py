import sys
input = sys.stdin.readline


def yaho(n, r, c, result):

    if n == 0:
        return result

    coord = [0, 0]

    if 2**(n-1) <= c:  # 중간보다 오른쪽에 있으면
        coord[1] = 1
    if 2**(n-1) <= r:  # 중간보다 아래에 있으면
        coord[0] = 1

    if coord == [0, 0]:
        return yaho(n-1, r, c, result)
    elif coord == [0, 1]:
        c -= 2**(n-1)
        result += 2**(2*n-2)
        return yaho(n-1, r, c, result)
    elif coord == [1, 0]:
        r -= 2**(n-1)
        result += 2**(2*n-2)*2
        return yaho(n-1, r, c, result)
    elif coord == [1, 1]:
        r -= 2**(n-1)
        c -= 2**(n-1)
        result += 2**(2*n-2)*3
        return yaho(n-1, r, c, result)


n, r, c = map(int, input().split())
print(yaho(n, r, c, 0))