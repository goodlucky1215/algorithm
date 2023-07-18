class Solution:
    def isValid(self, s: str) -> bool:
        result = []
        table = {
            ")" : "(",
            "]" : "[",
            "}" : "{"
        }
        for word in s :
            if word not in table:
                result.append(word)
            elif not result or table[word] != result.pop():
                return False
        return len(result)==0