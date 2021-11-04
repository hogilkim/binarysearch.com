# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        length = 0
        while node != None:
            node = node.next
            length += 1
        return length