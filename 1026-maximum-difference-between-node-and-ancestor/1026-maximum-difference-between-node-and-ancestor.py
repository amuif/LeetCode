# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:

        def get_max(node):
            if not node:
                return float("-inf"), float("inf"), 0

            l_max, l_min, l_ans = get_max(node.left)
            # go right
            r_max, r_min, r_ans = get_max(node.right)

            maxi = max(l_max , r_max, node.val)
            mini = min(l_min , r_min, node.val)
            ans = max(maxi-node.val, abs(mini - node.val), l_ans , r_ans )


            return maxi,mini,ans

        return  get_max(root)[-1]
    
