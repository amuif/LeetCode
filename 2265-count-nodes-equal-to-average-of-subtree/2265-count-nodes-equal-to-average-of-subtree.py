# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = 0

        def dfs(node):
            nonlocal ans
            if not node:
                return (0, 0)

            # count += 1
            # summed += node.val
            # gets the count and sum for subtree
            left_count, left_sum = dfs(node.left)
            right_count, right_sum = dfs(node.right)
            # calculates the subtree data
            current_sum = left_sum + right_sum + node.val
            current_count = left_count + right_count + 1

            if node.val == (current_sum // current_count):
                ans += 1

            return (current_count,current_sum)

        dfs(root)
        return ans
