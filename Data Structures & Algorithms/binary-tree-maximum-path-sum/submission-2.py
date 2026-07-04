# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float('inf')


        def maxBranchSum(root):
            nonlocal max_sum

            if root is None: return 0

            left_branch = maxBranchSum(root.left) 
            left_branch = left_branch if left_branch > 0 else 0
            right_branch = maxBranchSum(root.right)
            right_branch = right_branch if right_branch > 0 else 0
            min_branch = min(right_branch, left_branch)
            path_sum = root.val + left_branch + right_branch
            print(f"{left_branch} + {right_branch} = {path_sum}")
            max_sum = max(max_sum, path_sum)
            return path_sum - min_branch

        path_sum = maxBranchSum(root)
        max_sum = max(max_sum, path_sum)

        return max_sum
    