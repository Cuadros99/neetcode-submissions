# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [root]
        output = False

        while len(stack) > 0 and not output :
            node = stack.pop()
            if node.val == subRoot.val:
                output = self.isEqualTree(node, subRoot)

            if node.right: stack.append(node.right)
            if node.left: stack.append(node.left)

        return output


    def isEqualTree(self, r1: TreeNode, r2: TreeNode):
        if r1 is None and r2 is None:
            return True
        if r1 and r2 and r1.val == r2.val:
            return self.isEqualTree(r1.left, r2.left) and self.isEqualTree(r1.right, r2.right)
        else:
            return False
        