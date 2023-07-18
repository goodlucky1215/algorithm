class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        anwer = [0] * len(temperatures)
        stack = []
        for index, value in enumerate(temperatures) :
            while stack and value > temperatures[stack[-1]]:
                s = stack.pop()
                anwer[s] = index - s
            stack.append(index)
        return anwer