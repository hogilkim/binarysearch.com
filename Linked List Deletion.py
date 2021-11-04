# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, node, target):
        while node != None and node.val == target:
            node = node.next
        if node == None:
            return node

        curr = node.next
        prev = node
        while curr != None:
            if curr.val == target:
                prev.next = curr.next
            else: 
                prev=prev.next
            curr = curr.next
        return node