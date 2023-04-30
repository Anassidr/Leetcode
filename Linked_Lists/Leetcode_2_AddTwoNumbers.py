# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
import functools as ft
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
                push = 0
                ref = ListNode()
                res = ListNode()
                ref.next = res                 
                while l1 and l2:
                    s = 0
                    if l1:
                        s += l1.val
                    if l2:
                        s += l2.val
                    res.val = (s + push)%10
                    push = (s + push) // 10
                    if l1.next != None or l2.next != None:
                        res.next = ListNode(0)
                        res = res.next
                    l1 = l1.next
                    l2 = l2.next
                        
                while l1:
                    l1.val += push
                    res.val = l1.val%10 
                    push = l1.val//10
                    if l1.next != None:
                        res.next = ListNode(0)
                        res = res.next
                    l1 = l1.next
                    
                while l2:
                    l2.val += push
                    res.val = l2.val%10 
                    push = l2.val//10
                    if l2.next != None:
                        res.next = ListNode(0)
                        res = res.next
                    l2 = l2.next
                if push != 0:
                    res.next = ListNode(0)
                    res = res.next
                    res.val = push
                    
                return ref.next
                    