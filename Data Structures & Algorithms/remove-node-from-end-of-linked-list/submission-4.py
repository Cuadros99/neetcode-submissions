# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        r = head
        l = dummy
        counter = n

        while r:
            if counter > 0:
                r = r.next
            else:
                r = r.next
                l = l.next
            counter -= 1

        if l.next:
            l.next = l.next.next
        else:
            return None

        return dummy.next
