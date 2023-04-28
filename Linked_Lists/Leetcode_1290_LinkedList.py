# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.number = ""
    def getDecimalValue(self, head: ListNode) -> int:
        if head:
            self.number += str(head.val)
            return self.getDecimalValue(head.next)
        return int(self.number, 2)

