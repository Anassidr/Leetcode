# merge numbers between zeroes
# [0,3,1,0,4,5,2,0] to [4,11]

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        s = 0
        # keep a reference to the original linked list
        newhead = ListNode()
        newhead = head
        # pointers 
        ahead = head.next
        behind = head
        while ahead:
            if ahead.val == 0:
                ahead.val = s
                s = 0
                behind.next = ahead
                behind = behind.next
            else:
                s += ahead.val

            ahead = ahead.next
        return newhead.next
