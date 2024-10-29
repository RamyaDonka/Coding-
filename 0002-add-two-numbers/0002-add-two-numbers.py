# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1:[ListNode], l2:[ListNode]) -> [ListNode]:

        dummy_head = ListNode(0)  # Dummy head to start the new linked list
        current_node = dummy_head  # Pointer to traverse and build the new linked list
        carry_over = 0  # Keep track of carry-over

        while l1 or l2 or carry_over:
            # Get the current values (if the list node is None, use 0)
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate the sum and the new carry_over
            total = val1 + val2 + carry_over
            carry_over = total // 10  # Compute the new carry
            new_val = total % 10  # Get the digit to store in the new node

            # Create a new node with the sum and move the current_node forward
            current_node.next = ListNode(new_val)
            current_node = current_node.next

            # Move l1 and l2 to their next nodes, if available
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy_head.next