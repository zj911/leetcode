
def partition(li, left, right):
    tmp = li[left]
    while left < right:
        # 从右边开始循环找比第一个数小的数
        while left < right and li[right] >= tmp:
            right -= 1
        li[left] = li[right]

        # 从右边开始循环找比第一个数小的数
        while left < right and li[left] <= tmp:
            left += 1
        li[right] = li[left]
    li[left] = tmp
    return left


def quick_sort(li, left, right):
    if left < right:
        mid = partition(li, left, right)
        quick_sort(li, left, mid-1)
        quick_sort(li, mid+1, right)
