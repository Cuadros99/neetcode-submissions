# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head.next
        r_list = None

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        r_list = slow.next
        slow.next = None
        prev = None

        while r_list:
            tmp = r_list.next
            r_list.next = prev
            prev = r_list
            r_list = tmp
        
        r_list = prev
        curr = head

        while r_list:
            tmp_1, tmp_2 = curr.next, r_list.next
            curr.next = r_list
            curr.next.next = tmp_1
            r_list = tmp_2
            curr = curr.next.next
            

