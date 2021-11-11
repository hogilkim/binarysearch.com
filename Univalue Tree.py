# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return self.helper(root, root.val)
    def helper(self, node, val):
        if not node:
            return True
        return node.val == val and self.helper(node.left, val) and self.helper(node.right, val)
