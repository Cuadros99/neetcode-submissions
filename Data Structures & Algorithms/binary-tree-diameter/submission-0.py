# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        _, max_diameter = self.depthTree(root)
        return max_diameter
    


    def depthTree(self, root: Optional[TreeNode]):

        if root is None: 
            return 0, 0

        left_depth, left_diam = self.depthTree(root.left)
        right_depth, right_diam = self.depthTree(root.right)
        
        diameter = left_depth + right_depth
        max_diameter = max(left_diam, right_diam, diameter) 

        depth = max(left_depth, right_depth) + 1
        return depth, max_diameter
