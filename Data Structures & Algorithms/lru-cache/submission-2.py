class ListNode:
    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.next, self.prev = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.hashmap = {}
        self.left, self.right = ListNode(0,0), ListNode(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.count = 0
        self.cap = capacity

    def remove(self, node):

        node.prev.next =  node.next
        node.next.prev = node.prev
    
    def insert(self, node):
        self.right.prev.next = node
        node.prev = self.right.prev
        self.right.prev = node
        node.next = self.right

    def get(self, key: int) -> int:
        if key in self.hashmap:
            node = self.hashmap[key]
            self.remove(node)
            self.insert(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.hashmap:
            node = self.hashmap[key]
            node.val = value
            self.remove(node)
            self.insert(node)
        else:
            node = ListNode(key, value)
            self.hashmap[key] = node
            self.insert(node)
            self.count += 1

        if self.count > self.cap:
            rem_node = self.left.next
            self.remove(rem_node)
            del self.hashmap[rem_node.key]
            self.count -= 1
            
        
