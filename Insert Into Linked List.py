# class LLNode:
#     def __init__(self, val, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def solve(self, head, pos, val):
        if pos == 0:
            return_node = LLNode(val, next=head)
            return return_node

        insert_node_index = 1
        inserting_prev = head

        while insert_node_index != pos:
            inserting_prev = inserting_prev.next
            insert_node_index += 1
        inserting = LLNode(val)
        inserting_next = inserting_prev.next
        inserting_prev.next = inserting
        inserting.next = inserting_next
        return head