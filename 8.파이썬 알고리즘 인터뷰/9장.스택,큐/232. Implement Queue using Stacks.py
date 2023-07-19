import collections


class MyQueue:

    def __init__(self):
        self.input = []

    def push(self, x: int) -> None:
        return  self.input.append(x)

    def pop(self) -> int:
        r = input[0]
        output = []
        for i in range(1, len(self.input)) :
            output.append(self.input[i])
        self.input = output
        return r


    def peek(self) -> int:
        return self.input[-1]

    def empty(self) -> bool:
        return self.input() == [] and self.output() == []