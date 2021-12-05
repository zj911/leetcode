class Node:
    def __init__(self, item):
        self.item = item
        self.next = None


a = Node(1)
b = Node(2)
c = Node(3)
a.next = b
b.next = c

print(a.next.next.item)