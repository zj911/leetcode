class Queue:
    # 环形队列
    def __init__(self, size=100):
        self.queue = [0 for _ in range(size)]
        self.size = size
        self.rear = 0   # 队尾指针
        self.front = 0  # 队首指针

    def push(self, element):
        if not self.is_filled():
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = element
        else:
            raise IndexError('queue is filled')

    def pop(self):
        if not self.is_empty():
            self.front = (self.front + 1) % self.size
            return self.queue[self.front]
        else:
            raise IndexError('queue is empty')

    def is_empty(self):
        # 判断队空
        return self.rear == self.front

    def is_filled(self):
        # 判断队满
        return (self.rear + 1) % self.size == self.front
