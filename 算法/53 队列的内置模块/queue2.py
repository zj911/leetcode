from collections import deque

# 创建空队列
q = deque()
# 进队 队尾
q.append(1)
# 出队 队首
q.popleft()
# 进队 队首 -- 双向队列
q.appendleft(1)
# 出队 队尾 -- 双向队列
q.pop()


# 长度为5，大于5，则前面的自动出队
q = deque([1, 2, 3], 5)

# 实现tail命令查看后几行
def tail(n):
    with open('test.txt', 'r') as f:
        q = deque(f, n)
        return q


for line in tail(5):
    # 打印并去掉换行
    print(line, end='')