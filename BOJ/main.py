import sys

input = sys.stdin.readline

def binarySearch(trees, m):
    # 이분탐색으로 접근하려고 하니
    # 시작점과 끝점 설정
    left = 0
    right = max(trees)

    saw_height = 0  # 톱 높이

    # 원하는 목표 지점 찾을때까지 반복
    while left <= right:
        tree_heights = 0  # 절단된 나무 길이 총합
        mid = (left + right) // 2  # 중간점 설정

        # 절단된 나무 길이 합 계산하기
        for tree in trees:
            if tree > mid:
                tree_heights += tree - mid

        # 범위조정
        if tree_heights >= m:
            saw_height = mid
            left = mid + 1
        else:
            right = mid - 1

    return saw_height

# 입력부
n, m = map(int, input().split())
trees = list(map(int, input().split()))

# 출력부
print(binarySearch(trees, m))
