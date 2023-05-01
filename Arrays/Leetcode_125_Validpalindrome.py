# first solution, traversing twice 

class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""
        for x in s:
            if x.isalnum():
                new_s += x.lower()
        for i in range(len(new_s)//2):
            if new_s[i] != new_s[-(i+1)]:
                return False
        return True
    
# using pointers, not caring about transforming the string first
# just check if the characters of interest are palindroming


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1
        while l < r:
            while l < r and not s[r].isalnum():
                r -= 1 
            while l < r and not s[l].isalnum():
                l += 1
            if s[l].lower() != s[r].lower():
                return False
            l += 1
            r -= 1
        return True 
