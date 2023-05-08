

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        Charset = set()
        result = 0
        l = 0
        for r in range(len(s)):
            while s[r] in Charset:
                Charset.remove(s[l])
                l += 1 
            Charset.add(s[r])
            result = max(result, r - l + 1)

        return result
