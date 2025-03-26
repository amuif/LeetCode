# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # if p < root.val go left
        # if q  > root.val go right
        # whenever you get either of the values return immediatly

        def bst(node):
            if node is  None:
                return None

            if p.val < node.val and q.val< node.val:
                return bst(node.left)
            if p.val > node.val and q.val > node.val:
                return bst(node.right)
            return node

        return bst(root)
        # return output
        # print(output.val)
        # return output.val