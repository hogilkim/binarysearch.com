# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        return self.helper(root, 0)
    def helper(self, node, total_sum):
        if not node:
            return 0
        total_sum = 0
        total_sum += self.helper(node.left, total_sum)
        total_sum += self.helper(node.right, total_sum)
        total_sum += node.val
        return total_sum