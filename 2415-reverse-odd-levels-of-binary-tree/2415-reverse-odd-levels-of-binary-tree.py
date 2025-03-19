# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # get the odd levels then reverse
        def swapp_val(left,right,parity):
            if not left:
                return 
                
            if parity % 2 != 0:
                left.val , right.val = right.val , left.val

            swapp_val(left.left, right.right, parity + 1)
            swapp_val(left.right, right.left, parity + 1)

        swapp_val(root.left, root.right, 1)
        return root   



