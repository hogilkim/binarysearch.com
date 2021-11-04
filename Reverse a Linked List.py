# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node):
        if node == None or node.next == None:
            return node
        
        curr = node.next
        prev = node
        prev.next = None
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        # 1 -> 2 -> 3 -> 4 -> 5
        return prev 