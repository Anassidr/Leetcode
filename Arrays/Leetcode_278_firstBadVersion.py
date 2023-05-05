# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion():
    return

# using binary search 

class Solution:
    def firstBadVersion(self, n: int) -> int:
        low = 0
        high = n-1 
        while low <= high:
            middle = (low+high)//2
            if isBadVersion(middle) == False and isBadVersion(middle+1) == True:
                return middle+1
            elif isBadVersion(middle) == False:
                low = middle + 1 
            elif isBadVersion(middle) == True:
                high = middle
