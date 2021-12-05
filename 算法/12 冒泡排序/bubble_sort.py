def bubble_sort(li):
    # 冒泡排序
    # 运行 len(li) - 1躺
    for i in range(len(li)-1):
        # 是否交换标志位，如果不交换就是已经排序完成
        exchange = False
        for j in range(len(li) - i - 1):
            # len(li) - i - 1 交换的数值 -- 箭头位置范围
            if li[j] > li[j+1]:
                # 交换数值
                li[j], li[j+1] = li[j+1], li[j]
                exchange = True
        if not exchange:
            return
