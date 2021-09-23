# 680. Valid Palindrome II (Easy)
from typing import List

class Solution:
    def isPalindrome(self, s:str) -> bool:
        i, j = 0, len(s) - 1
        while i <= j:
            if s[i] != s[j]:
                return False
            i += 1
            j -= 1
        return True
    
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
               return self.isPalindrome(s[i+1 : j+1]) or self.isPalindrome(s[i: j])
        return True

