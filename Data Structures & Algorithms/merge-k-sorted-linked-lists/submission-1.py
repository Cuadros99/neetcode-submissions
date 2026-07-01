# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        dummy = ListNode(None)
        curr_output = dummy
        
        while any(lists):
            min_val = [0, float('inf')]
            for i, n in enumerate(lists):
                if n and min_val[1] > n.val:
                    min_val = (i, n.val)
            
            max_node = lists[min_val[0]]
            curr_output.next = ListNode(min_val[1])
            curr_output = curr_output.next
            lists[min_val[0]] = max_node.next
            
                
        return dummy.next



        