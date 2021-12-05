

def hanoi(n, a, b, c):
    if n > 0:
        hanoi(n-1, a, c, b)
        print("moving from {} to {}".format(a, c))
        hanoi(n-1, b, a, c)

# def hanoi(n,a,b,c):
#     if n>0:
#         hanoi(n-1,a,c,b)
#         print("把 %s 号圆盘从  %s 位置移动到 %s 位置" % (n,a,c))
#         hanoi(n-1,b,a,c)
# hanoi(3,A柱,B柱,C柱)


hanoi(3, 'A', 'B', 'C')
