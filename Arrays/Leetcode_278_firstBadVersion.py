# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion():
    return

# using binary search 
# time complexity O(log n)
# space complexity O(1)


class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n-1 
        while low <= high:
            #  avoid integer overflow 
            middle = low +(high-low)//2
            if not isBadVersion(middle):
                low = middle + 1 
            else:
                high = middle - 1
        return low
