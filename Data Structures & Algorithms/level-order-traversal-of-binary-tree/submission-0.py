# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        output = [[root.val]]
        queue = deque([root, TreeNode(None)])
        level = []
        while queue:
            node = queue.popleft()
            if node.left: 
                queue.append(node.left)
                level.append(node.left.val)
            if node.right: 
                queue.append(node.right)
                level.append(node.right.val)
            if node.val is None and level:
                output.append(level)
                queue.append(TreeNode(None))
                level = []
            
        
        return output



