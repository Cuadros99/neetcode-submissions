# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        prev = None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        curr = prev
        prev = None
        counter = 1

        while curr:
            if counter == n:
                curr = curr.next
            else:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp
                
            counter += 1
        
        return prev
            
