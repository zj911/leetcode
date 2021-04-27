'''
762. 二进制表示中质数个计算置位
给定两个整数 L 和 R ，找到闭区间 [L, R] 范围内，计算置位位数为质数的整数个数。

（注意，计算置位代表二进制表示中1的个数。例如 21 的二进制表示 10101 有 3 个计算置位。还有，1 不是质数。）

示例 1:

输入: L = 6, R = 10
输出: 4
解释:
6 -> 110 (2 个计算置位，2 是质数)
7 -> 111 (3 个计算置位，3 是质数)
9 -> 1001 (2 个计算置位，2 是质数)
10-> 1010 (2 个计算置位，2 是质数)

'''


# 暴力排查出质数，取结果
class Solution:
    def countPrimeSetBits(self, L: int, R: int) -> int:
        t = []
        for i in range(1, 21):
            count = 0
            for j in range(1, i + 1):
                if i % j == 0:
                    count += 1
                    if count > 2:
                        break
            if count == 2:
                t.append(i)
        t2 = [i for i in range(L, R + 1) if bin(i)[2:].count('1') in t]
        return len(t2)


# 正解
class Solution2():
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        res = 0
        prime = [2, 3, 5, 7, 11, 13, 17, 19]
        for i in range(L, R + 1):
            if bin(i).count('1') in prime:
                res += 1
        return res
