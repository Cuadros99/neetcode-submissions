"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        hashmap = {}
        curr = head
        new_head = Node(head.val)
        new_curr = new_head
        hashmap[head] = new_head
        
        while curr:
            curr = curr.next
            if curr:
                new_curr.next = Node(curr.val)
                new_curr = new_curr.next
                hashmap[curr] = new_curr
            

        new_curr = new_head
        curr = head
        
        while new_curr:
            if curr.random:
                new_curr.random = hashmap[curr.random]
            
            new_curr = new_curr.next
            curr = curr.next
                
        return new_head

            