# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        hash_set = set()
        node = head
        index = -1
        counter = 0

        while node:
            if node in hash_set:
                index = counter
                return True
            else:
                hash_set.add(node)
                node = node.next
            counter += 1
            
        return False
        



        
        