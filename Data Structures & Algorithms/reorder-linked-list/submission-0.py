# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        curr, r_node = head, head
        stack = []
        tmp = None

        while r_node.next:
            r_node = r_node.next
            stack.append(r_node)

        while stack and curr != stack[-1]:
            tmp = curr.next
            curr.next = stack.pop()
            curr.next.next = tmp
            curr = tmp
            

        curr.next = None
