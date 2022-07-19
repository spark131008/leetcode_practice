from collections import deque


class MyStack:

    def __init__(self):
        self.dq = deque([])

    def push(self, x: int) -> None:
        self.dq.append(x)

    def pop(self) -> int:
        return self.dq.pop()

    def top(self) -> int:
        return self.dq[-1]

    def empty(self) -> bool:
        if not self.dq:
            return True
        else:
            return False