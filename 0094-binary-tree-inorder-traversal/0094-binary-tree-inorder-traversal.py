# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def recurs(root):

            if root:
                recurs(root.left)
                res.append(root.val)
                recurs(root.right)

        recurs(root)
        return res
