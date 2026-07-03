# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0
        self.depthTree(root)
        return self.max_diameter
    


    def depthTree(self, root: Optional[TreeNode]):

        if root is None: 
            return 0

        left_depth = self.depthTree(root.left)
        right_depth = self.depthTree(root.right)
        
        diameter = left_depth + right_depth
        self.max_diameter = max(self.max_diameter, diameter) 

        depth = max(left_depth, right_depth) + 1
        return depth
