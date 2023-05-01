class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        mymap={}
        for x in s:
            if x in mymap:
                mymap[x] += 1
            else:
                mymap[x] = 1
        for x in t: 
            if x in mymap:
                mymap[x] -=1
                if mymap[x] < 0:
                    return False
            else:
                return False
        return len(t) == len(s) 