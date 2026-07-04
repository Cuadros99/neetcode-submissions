# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        return self.isValidSubTree(root, -float('inf'), float('inf'))
        

    def isValidSubTree(self, root, l_lim, r_lim):
        left_res, right_res = True, True

        if root.left:
            if root.left.val < root.val and root.left.val > l_lim:
                left_res = self.isValidSubTree(root.left, l_lim, root.val)
            else:
                left_res = False

        if root.right:
            if root.right.val > root.val and root.right.val < r_lim:
                right_res = self.isValidSubTree(root.right, root.val, r_lim)
            else:
                right_res = False

        return right_res and left_res


    
