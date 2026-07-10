class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

class MedianFinder:

    def __init__(self):
        self.dummy = ListNode(float('-inf'), None)
        self.lenght = 0

    def addNum(self, num: int) -> None:
        curr = self.dummy
        while curr:
            if curr.next and num <= curr.next.val:
                curr.next = ListNode(num, curr.next)
                break
            elif curr.next and num > curr.next.val:
                curr = curr.next
            else:
                curr.next = ListNode(num, None)
                break
        self.lenght += 1


    def findMedian(self) -> float:
        if self.lenght % 2:
            counter = self.lenght // 2 + 1
            if self.dummy.next:
                return self.getNNode(counter, self.dummy.next)
            else:
                return None
        else:
            counter = self.lenght // 2
            if self.dummy.next:
                sum_res = self.getNNode(counter, self.dummy.next) + self.getNNode(counter + 1, self.dummy.next)
                return sum_res/2
            else:
                return None
        
    def getNNode(self, n, root):
        curr = root
        while curr:
            n -= 1
            if n == 0:
                return curr.val
            curr = curr.next
        return None
