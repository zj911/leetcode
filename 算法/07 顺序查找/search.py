
def linear_search(li, val):
    # 顺序查找
    for index, v in enumerate(li):
        if v == val:
            return index
        else:
            return None


def binarty_search(li, val):
    # 二分查找
    left = 0
    right = len(li) - 1
    while left <= right:
        # 说明候选区域有值
        mid = (left + right) // 2
        if li[mid] == val:
            return mid
        elif li[mid] > val:
            right = mid - 1
        elif li[mid] < val:
            left = mid + 1
    else:
        return None
