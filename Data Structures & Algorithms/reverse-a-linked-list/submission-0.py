# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        this_node = head
        previous_node = None
        next_node = None

        while this_node:
            next_node = this_node.next
            this_node.next = previous_node
            previous_node = this_node
            this_node = next_node
            

        return previous_node