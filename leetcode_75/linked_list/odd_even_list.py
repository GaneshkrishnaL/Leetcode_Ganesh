from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val: int = 0, next: 'Optional[ListNode]' = None):
        """
        Initialize a new node with a value and an optional next pointer.

        :param val: The integer value stored in the node.
        :param next: Reference to the next node in the list.
        """
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Rearrange a singly linked list such that all nodes at odd positions are
        grouped together followed by the nodes at even positions.

        The relative order of the nodes within the odd and even groups is preserved.
        The algorithm runs in O(n) time using O(1) additional space.

        :param head: The head of the singly linked list.
        :return: The head of the rearranged list.
        """
        # If the list is empty or contains only one node, no reordering is needed.
        if not head or not head.next:
            return head

        # Initialize two pointers:
        # 'lag' will point to the current odd node,
        # 'lead' will point to the current even node.
        lag = head                 # Start of the odd-indexed nodes.
        lead = head.next           # Start of the even-indexed nodes.
        even_head = lead           # Save the head of even list to connect later.

        # Iterate through the list until we reach the end of the even-indexed nodes.
        while lead and lead.next:
            # Connect the current odd node to the next odd node.
            lag.next = lead.next
            lag = lag.next  # Move 'lag' to the next odd node.

            # Connect the current even node to the next even node.
            lead.next = lag.next
            lead = lead.next  # Move 'lead' to the next even node.

        # After reordering, append the even-indexed nodes after the odd-indexed nodes.
        lag.next = even_head
        return head
