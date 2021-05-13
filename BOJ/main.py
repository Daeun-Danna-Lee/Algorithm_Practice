import sys

input = sys.stdin.readline

# 입력부
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 이분탐색으로 접근하려고 하니
# 시작점과 끝점 설정
left = 0
right = max(trees)

# 원하는 목표 지점 찾을때까지 반복
while left <= right:
    tree_heights = 0  # 절단된 나무 길이 총합
    mid = (left + right) // 2  # 중간점 설정

    # 뭔가 이 반복문 부분 때문에 시간 초과 느낌..
    # 절단된 나무 길이 합 계산하기
    for tree in trees:
        if tree > mid:
            tree_heights += tree - mid

        # 범위조정
    if tree_heights >= m:
        left = mid + 1
    else:
        right = mid - 1

print(right)