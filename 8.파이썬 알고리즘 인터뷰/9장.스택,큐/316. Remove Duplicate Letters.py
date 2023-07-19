import collections


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        su, stack, set_word = collections.Counter(s),[], set()
        for i in s:
            su[i] -=1
            if i in set_word:
                continue
            while stack and i<stack[-1] and su[stack[-1]]>0:
                set_word.remove(stack.pop())
            stack.append(i)
            set_word.add(i)
        return ''.join(stack)

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        for word in sorted(set(s)):
            suffix = s[s.index(word):]
            if set(s) == set(suffix) :
                return word+self.removeDuplicateLetters(suffix.replace(word,''))
        return ''