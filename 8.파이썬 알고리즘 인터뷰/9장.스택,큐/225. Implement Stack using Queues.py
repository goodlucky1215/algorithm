import collections


class MyStack:

    def __init__(self):
        self.q = collections.deque()

    def push(self, x: int) -> None:
        return self.q.appendleft(x)

    def pop(self) -> int:
        return self.q.popleft()


    def top(self) -> int:
        return self.q.index(0)

    def empty(self) -> bool:
        return len(self.q) == 0
