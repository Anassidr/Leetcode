# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.count = 0
        self.map = {}
    def middleNode(self, head: ListNode) -> ListNode:
        if head:
            self.count += 1 
            self.map[self.count] = head
            return self.middleNode(head.next)
        return self.map[(self.count//2)+1]


# other solution 

def middleNode(self, head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow