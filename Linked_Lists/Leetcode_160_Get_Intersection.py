# return the node at which the two lists intersect 

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def __init__(self):
        self.amap = {}
        self.bmap = {}
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        while headA or headB:
            if headA in self.bmap or headA==headB:
                return headA
            elif headB in self.amap:
                return headB
            self.amap[headA] = headA
            self.bmap[headB] = headB

            if headA:
                headA = headA.next
            if headB:
                headB = headB.next
        return None