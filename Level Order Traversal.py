# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root):
        visited = set()
        node_to_visit = [root]
        result = []

        def bfs(node):
            if node not in visited:
                result.append(node.val)
                visited.add(node)
            if node.left:
                node_to_visit.append(node.left)
            if node.right:
                node_to_visit.append(node.right)
            
        while node_to_visit:
            bfs(node_to_visit.pop(0))
        return result