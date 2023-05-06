class Solution:
    def insert(self, intervals, newInterval):
        res = []
        for i in range(len(intervals)):
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                # if the current interval doesn't overlap at all, just add it and keep going
                res.append(intervals[i])
            else:
                # newInterval keeps being overwritten until it finds its spot, then we add it and return 
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        # in case newinterval belongs at the end and we didn't add it yet 
        res.append(newInterval)
        return res