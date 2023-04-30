# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                push = 0
                ref = ListNode()
                res = ListNode()
                ref.next = res                 
                while l1 or l2 or push != 0:
                    s = 0
                    if l1:
                        s += l1.val
                        l1 = l1.next
                    if l2:
                        s += l2.val
                        l2 = l2.next

                    res.val = (s + push)%10
                    push = (s + push) // 10
                    if l1 or l2 or push != 0:
                        res.next = ListNode(0)
                        res = res.next
                    
                return ref.next
                    