"""
7. 整数反转
给你一个 32 位的有符号整数 x ，返回将 x 中的数字部分反转后的结果。
如果反转后整数超过 32 位的有符号整数的范围[−231, 231− 1] ，就返回 0。
假设环境不允许存储 64 位整数（有符号或无符号）。
示例 1：
输入：x = 123
输出：321
示例 2：
输入：x = -123
输出：-321
示例 3：
输入：x = 120
输出：21
示例 4：
输入：x = 0
输出：0
"""

# 注意输入为0的情况
import math
class Solution:
    def reverse(self, x: int) -> int:
        x = str(x)
        if x == '0':
            return 0
        if x.startswith('-'):
            x = x[1:][::-1].lstrip('0')
            x = '-' + x
        else:
            x = x[::-1].lstrip('0')
        if int(x) < - math.pow(2, 31) or int(x) >  math.pow(2, 31) - 1:
            return 0
        else:
            return int(x)


