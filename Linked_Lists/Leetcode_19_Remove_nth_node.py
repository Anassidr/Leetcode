# remove nth node from the end of the list

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        reference = head
        mymap = {}
        i = 1
        while head:
            mymap[i] = head
            head = head.next
            i += 1 
        target = i - n - 1
        if target == 0:
            return reference.next
        if mymap[target].next:
            mymap[target].next = mymap[target].next.next
        else:
            mymap[target].next = None

        return reference
        
