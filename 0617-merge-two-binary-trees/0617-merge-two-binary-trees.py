# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        def recurse(root1,root2):
            if root1 and root2:
                root = TreeNode(root1.val + root2.val)
                root.left = recurse(root1.left,root2.left)
                root.right = recurse(root1.right,root2.right)
                return root
            else:
                return root1 or root2

        return recurse(root1,root2)
        
            
        