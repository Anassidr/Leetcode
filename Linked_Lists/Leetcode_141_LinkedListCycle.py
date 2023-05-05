# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# approach : use hashmap. 
# Complexity O(n) time and O(n) space
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        mymap = {}
        while head:
            if head.next in mymap:
                return True
            mymap[head] = True
            head = head.next
        return False
    

# pretty clever approach
# Using two pointers fast and slow 
# They will eventually meet because the distance between them is reduced by 1 at each iteration
# O(n) time and O(1) space

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


testt = []

testt.append(1)

testt.pop()
print(testt)