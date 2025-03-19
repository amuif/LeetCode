# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        ans = defaultdict(lambda: float("-inf"))

        def get_max(node, level ):
            if not node:
                return


            ans[level] = max(node.val, ans[level])         
            

            get_max(node.left,level+1)
            get_max(node.right, level+1)


        get_max(root, 0)
        return list(ans.values())
        
        