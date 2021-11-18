# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# class Solution:
#     def solve(self, root):
#         self.helper(root)
#         return root
#     def helper(self, node):
#         if node:
#             temp = node.left
#             node.left = node.right
#             node.right = temp
#             self.helper(node.left)
#             self.helper(node.right)
        

class Solution:
    def solve(self, root):
        if not root: return None

        # A,B = B,A
        root.left, root.right = self.solve(root.right), self.solve(root.left)
        
        return root