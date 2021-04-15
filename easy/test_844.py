"""
844. 比较含退格的字符串

给定 S 和 T 两个字符串，当它们分别被输入到空白的文本编辑器后，判断二者是否相等，并返回结果。 # 代表退格字符。

注意：如果对空文本输入退格字符，文本继续为空。

 

示例 1：

输入：S = "ab#c", T = "ad#c"
输出：true
解释：S 和 T 都会变成 “ac”。
示例 2：

输入：S = "ab##", T = "c#d#"
输出：true
解释：S 和 T 都会变成 “”。
示例 3：

输入：S = "a##c", T = "#a#c"
输出：true
解释：S 和 T 都会变成 “c”。
示例 4：

输入：S = "a#c", T = "b"
输出：false
解释：S 会变成 “c”，但 T 仍然是 “b”。
 

提示：

1 <= S.length <= 200
1 <= T.length <= 200
S 和 T 只含有小写字母以及字符 '#'。
 

进阶：

你可以用 O(N) 的时间复杂度和 O(1) 的空间复杂度解决该问题吗？
"""

# 解法：遇到#则删除尾部，不是就加到列表，队列的使用
# 难点：判断出#开头的内容
class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        dic1 = []
        dic2 = []
        for i in S:
            if i != '#':
                dic1.append(i)
            elif i == '#' and dic1 != []:
                dic1.pop()
        for i in T:
            if i != '#':
                dic2.append(i)
            elif i == '#' and dic2 != []:
                dic2.pop()
        return dic1 == dic2