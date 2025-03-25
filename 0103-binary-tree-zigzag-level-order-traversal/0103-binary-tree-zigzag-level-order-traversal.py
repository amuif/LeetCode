# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []

        def zigzag(node,level):
            if node is None:
                return
            if len(output) <= level:
                output.append([])
            
            if level % 2 == 0:
                output[level].append(node.val)
            else:
                output[level].insert(0,node.val)

            zigzag(node.left,level+1)
            zigzag(node.right,level+1)

        zigzag(root,0)
        return output
                
        