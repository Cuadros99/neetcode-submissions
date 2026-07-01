# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        curr = [node for node in lists]
        dummy = ListNode(None)
        curr_output = dummy
        
        while any(curr):
            min_val = [0, float('inf')]
            for i, n in enumerate(curr):
                if n and min_val[1] > n.val:
                    min_val = (i, n.val)
            
            max_node = curr[min_val[0]]
            curr_output.next = ListNode(min_val[1])
            curr_output = curr_output.next
            curr[min_val[0]] = max_node.next
            
                
        return dummy.next



        