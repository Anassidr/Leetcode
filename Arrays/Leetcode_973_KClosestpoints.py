# time complexity : O(nlogn) because python uses the Timsort algorithm for sorting  

import math 
class Solution:
    def kClosest(self, points, k: int):
        def euclidean(x,y):
            return math.sqrt(x**2+y**2)
        result = []
        for point in points:
            result.append(
                [point,euclidean(point[0],point[1])]
                )
        result.sort(key=lambda x:x[1])
        res = []
        for i in range(k):
            res.append(result[i][0])

        return res
    

# slightly better approach using heaps to have O(klogn) complexity
import heapq
class Solution:
    def kClosest(self, points, k: int):
        minHeap = []
        for [x,y] in points:
            eucl = x**2+y**2
            minHeap.append(eucl,x,y)
        heapq.heapify(minHeap)
        res = []
        while k > 0:
            eucl, x, y = heapq.heappop(minHeap)
            res.append([x,y])
            k -= 1

        return res



