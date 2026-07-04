# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None

        hashmap = {}
        dummy = TreeNode(None)
        curr = dummy
        left = True
        p, i = 0, 0

        while p < len(preorder):
            val = preorder[p]
            next_node = TreeNode(val)
            p += 1

            if left:
                curr.left = next_node
            else:
                curr.right = next_node
                left = True

            curr = next_node
            
            hashmap[val] = next_node

            while i < len(preorder) and inorder[i] in hashmap:
                curr = hashmap[inorder[i]]
                i += 1
                left = False

        return dummy.left

            
                
                

            
                



