# solution 1 
class Solution:
    def twoSum(self, nums: int, target: int) -> int:
        mymap = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in mymap:
                return [mymap[diff], i]
            mymap[nums[i]] = i 

# using enumerate
class Solution:
    def twoSum(self, nums: int, target: int) -> int:
        PrevMap={}
        for i, n in enumerate(nums):
            diff = target - nums[i]
            if diff in PrevMap:
                return [PrevMap[diff], i]
            PrevMap[n] = i
        return 