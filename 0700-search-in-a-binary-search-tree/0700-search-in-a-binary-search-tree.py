# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:

        def search(node,number):
            if node is None:
                return None
            if node.val == number:
                return node
            if node.val > number:
                return search(node.left,number)
            if node.val < number:
                return search(node.right,number)

        return search(root,val)
        
        