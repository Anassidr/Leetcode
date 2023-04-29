# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        newhead = ListNode()
        # keeping track of the reference to the original node
        newhead.next = head

        mymap = {head:head}

        # using two pointers for traversal

        prev = newhead
        cur = head
        while cur:
            if cur.val in mymap:
                # prev being a pointer, we are changing the next attribute of the actual node in newhead
                # the node.next attribute is mutable
                prev.next = cur.next
            else:
                prev = cur
                mymap[cur.val] = True
            cur = cur.next
        return newhead.next


