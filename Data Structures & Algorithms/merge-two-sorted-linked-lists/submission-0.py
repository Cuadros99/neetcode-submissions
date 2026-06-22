# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        n1 = list1
        n2 = list2

        if not n1:
            return n2
        if not n2:
            return n1
            
        if n1.val <= n2.val:
            start = n1
            n1 = n1.next
        else:
            start = n2
            n2 = n2.next
        
        curr = start

        while n1 or n2:

            if not n1:
                curr.next = n2
                n2 = n2.next
            elif not n2:
                curr.next = n1
                n1 = n1.next
            elif n1.val <= n2.val:
                curr.next = n1
                n1 = n1.next
            else:
                curr.next = n2
                n2 = n2.next
            curr = curr.next

        return start
