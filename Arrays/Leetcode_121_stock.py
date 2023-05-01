# best time to buy and sell stock

# we don't need to keep track of all the possible pairs
# we update the best price difference as we go

class Solution:
    def maxProfit(self, prices: int) -> int:
        diff = 0 
        low = prices[0]
        for x in prices:
            if x - low > diff:
                diff = x-low
            if x < low:
                low = x
        return diff


                    