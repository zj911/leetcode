class Stack:
    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        self.stack.pop()

    def get_pop(self):
        if not self.stack:
            return self.stack[-1]
        else:
            return None

    def is_empty(self):
        return len(self.stack) == 0


def brace_match(s):
    # 判断括号是否匹配
    match = {")":"(", ']':'[', "}":"{"}
    stack = Stack()
    for ch in s:
        if ch in {"(", "[", "{"}:
            stack.push(ch)
        else:
            if stack.is_empty():
                return False
            elif stack.get_pop() == match.get(ch):
                stack.pop()
            else:
                return False
    if stack.is_empty():
        return True
    else:
        return False




