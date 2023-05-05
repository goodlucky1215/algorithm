class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_len = len(s) - 1
        for i in range(0,len(s)//2):
            if(s[i]!=s[s_len-i]) : return False
        return True