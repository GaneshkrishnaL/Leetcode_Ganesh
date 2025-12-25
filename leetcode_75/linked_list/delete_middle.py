# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Delete the middle node of a singly linked list and return the head of the modified list.  
        The "middle" node is determined using 0-based indexing such that if the list has n nodes,  
        the node at index n // 2 (floor division) is removed. For example:  
        - For a list of length 1, the middle node is the only node; deleting it results in an empty list.  
        - For a list of length 2, the second node (index 1) is considered the middle.  
        This function uses the fast and slow pointer technique to find the middle node in a single pass.
        """

        # Edge case: If the list is empty or contains only one node, removing the middle node yields an empty list.
        if not head or not head.next:
            return None

        # Initialize two pointers:  
        # "slow" will move one step at a time,  
        # "fast" will move two steps at a time.  
        # When "fast" reaches the end, "slow" will point to the middle node.
        slow = head
        fast = head

        # "prev" will keep track of the node immediately before "slow" so we can unlink the middle node.
        prev = None

        # Traverse the list using the fast and slow pointers.  
        # Continue looping while "fast" and "fast.next" are not None:  
        # - Advance "prev" to the current "slow" node.  
        # - Move "slow" forward by one node.  
        # - Move "fast" forward by two nodes.  
        # When the loop exits, "slow" will be at the middle node to remove, and "prev" will be just before it.
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        # At this point:  
        # - "slow" points to the middle node that needs to be removed.  
        # - "prev" points to the node before the middle node.  
        # To remove the middle node, skip it by pointing prev.next to slow.next.
        prev.next = slow.next

        # Return the head of the modified linked list.
        return head
