from collections import deque

maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 1, 0, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 1, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 0, 1, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 1, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

dirs = [
    lambda x, y: (x+1, y),
    lambda x, y: (x-1, y),
    lambda x, y: (x, y-1),
    lambda x, y: (x, y+1),
]

def print_r(path):
    curNode = path[-1]
    real_path = []
    while curNode[2] != -1:
        real_path.append(curNode[0:2])
        curNode = path[curNode[2]]
    real_path.append(curNode[0:2]) # 添加起点
    real_path.reverse()
    for i in real_path:
        print(i)


def maze_path_queue(x1, y1, x2, y2):
    queue = deque()
    queue.append((x1, y1, -1))
    path = []
    while len(queue) > 0:
        curNode = queue.popleft()
        path.append(curNode)
        if curNode[0] == x2 and curNode[1] == y2:
            # 找到终点
            print_r(path)
            return True
        for dir in dirs:
            nexrNode = dir(curNode[0], curNode[1])
            if maze[nexrNode[0]][nexrNode[1]] == 0:
                # 获取的是curNode再path里面的下标，后续节点进队，记录带它进来的节点
                queue.append((nexrNode[0], nexrNode[1], len(path) -1))
                maze[nexrNode[0]][nexrNode[1]] = 2 # 标记为2表示走过
    else:
        print('没有路')
        return False


maze_path_queue(1, 1, 8, 8)