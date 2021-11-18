# class Tree:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solve(self, root0, root1):

        def get_leaves_left_to_right(root):
            leaves = []
            stack = []
            stack.append(root)

            while stack:
                cur_node = stack.pop()

                if not cur_node.left and not cur_node.right:
                    leaves.append(cur_node.val)
                if cur_node.right:
                    stack.append(cur_node.right)
                if cur_node.left:
                    stack.append(cur_node.left)
                
            return leaves
        

        

            
        return get_leaves_left_to_right(root0) == get_leaves_left_to_right(root1)









        # root0_leaves = []
        # root1_leaves = []

        # def dfs(node, result):
        #     if not node.left and not node.right:
        #         root0_leaves.append(node.val)
        #     if node.left:
        #         dfs(node.left, result)
        #     if node.right:
        #         dfs(node.right, result)
        
        # dfs(root0, root0_leaves)
        # dfs(root1, root1_leaves)
        # print(root0_leaves)
        # print(root1_leaves)
        # return root0_leaves == root1_leaves

        # def dfs(node1, node2):
        #     if (not node1.left) and (not node1.right) and (not node2.left) and (not node2.right):
        #         return node1.val == node2.val
            
        #     node1_next = None
        #     node2_next = None
        #     if node1.left:
        #         node1_next = node1.left
        #     elif node1.right:
        #         node1_next = node1.right
        #     if node2.left:
        #         node2_next = node2.left
        #     elif node2.right:
        #         node2_next = node2.right
        #     if not node1_next or not node2_next:
        #         return False
        #     return dfs(node1_next, node2_next)

        # return dfs(root0.left, root1.left) and dfs(root0.right, root1.right)