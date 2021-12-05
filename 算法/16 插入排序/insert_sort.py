
def insert_sort(li):
    # i 表示摸到的无序区
    for i in range(1, len(li)):
        # j 为手里牌的下标
        j = i - 1
        tmp = li[i]
        while li[j] > tmp and j >= 0:
            # 手中的有序区向右移使得可以插入
            li[j+1] = li[j]
            j -= 1
        li[j + 1] = tmp


