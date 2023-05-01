class Solution:
    def containsDuplicate(self, nums: int) -> bool:
        mymap = {}
        for x in nums:
            if x in mymap:
                return True
            mymap[x] = True
        return False