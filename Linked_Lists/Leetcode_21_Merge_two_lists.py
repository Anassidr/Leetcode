# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, node1: ListNode, node2: ListNode) -> ListNode:
        dummy = ListNode(0)
        # set a pointer to the head of the new linked list
        cur = dummy
        
        while node1 and node2:
            if node1.val <= node2.val:
                cur.next = node1
                node1 = node1.next
            else:
                cur.next = node2
                node2 = node2.next
            cur = cur.next
        
        # append any remaining nodes from node1 or node2
        if node1:
            cur.next = node1
        elif node2:
            cur.next = node2
        
        # return the head of the new linked list
        return dummy.next