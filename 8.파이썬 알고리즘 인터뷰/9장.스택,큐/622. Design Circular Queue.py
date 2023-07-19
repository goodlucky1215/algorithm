import collections


class MyCircularQueue:

    def __init__(self, k: int):
        self.q = [None]*k
        self.q1 = 0
        self.q2 = 0
        self.lenk = k

    def enQueue(self, value: int) -> bool:
        if self.isFull() :
            return False
        self.q[self.q2] = value
        self.q2 = (self.q2+1)%self.lenk
        return True

    def deQueue(self) -> bool:
        if self.isEmpty() :
            return False
        self.q[self.q1] = None
        self.q1 = (self.q1 + 1) % self.lenk
        return True

    def Front(self) -> int:
        if self.isEmpty() :
            return -1
        else :
            return self.q[self.p1]

    def Rear(self) -> int:

        if self.isEmpty() :
            return -1
        else :
            return self.q[self.p2-1]

    def isEmpty(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is None

    def isFull(self) -> bool:
        return self.q1 == self.q2 and self.q[self.q1] is not None
