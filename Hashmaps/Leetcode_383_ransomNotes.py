class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        letters = {}
        for x in magazine:
            if x in letters:
                letters[x] += 1 
            else:
                letters[x] = 1
        for x in ransomNote:
            if x in letters:
                letters[x] -= 1
                if letters[x] < 0:
                    return False
            else:
                return False
        return True
