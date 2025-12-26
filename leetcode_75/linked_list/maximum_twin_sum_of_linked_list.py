# Problem: Maximum Twin Sum of a Linked List
# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/
#
# Approach:
# 1. Use the fast and slow pointer technique to find the middle of the linked list.
#    The `slow` pointer moves one node at a time, while the `fast` pointer moves two nodes at a time.
#    When `fast` reaches the end of the list, `slow` will be at the middle.
# 2. Reverse the second half of the linked list starting from the middle.
#    This allows us to easily pair the first half and the reversed second half to compute twin sums.
# 3. Traverse both halves simultaneously:
#    - For each pair of nodes (one from the first half and one from the reversed second half),
#      compute the sum of their values.
#    - Keep track of the maximum twin sum encountered.
# 4. Return the maximum twin sum.
#
# Complexity Analysis:
# - Time Complexity: O(n), where n is the number of nodes in the linked list.
#   We traverse the list a constant number of times (to find the middle, reverse the second half,
#   and compute twin sums).
# - Space Complexity: O(1), since we do not use any extra data structures; we only manipulate pointers.
#
# Example Walkthrough:
# Consider the linked list: [5, 4, 2, 1]
# 1. Use fast/slow pointers to find the middle: `slow` will point to the node with value 2.
# 2. Reverse the second half starting from `slow`:
#    Before reversing, the list looks like: 5 -> 4 -> 2 -> 1
#    After reversing the second half: 5 -> 4, and reversed part: 1 -> 2
#    Now we have two lists: first half head points to 5, second half head (prev) points to 1
# 3. Traverse both halves:
#    - Pair 5 (from first) and 1 (from second): twin sum = 5 + 1 = 6
#    - Pair 4 (from first) and 2 (from second): twin sum = 4 + 2 = 6
#    The maximum twin sum encountered is 6.
# 4. Return 6.
#
# Definition for singly-linked list is provided by LeetCode and assumed to be available:
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional

class Solution:
    def pairSum(self, head: Optional['ListNode']) -> int:
        """
        Compute the maximum twin sum of a singly linked list.

        A twin pair is defined as the ith node from the start and the ith node from the end (1-indexed).
        This function finds the maximum sum of all such twin pairs.

        :param head: The head of the singly linked list.
        :return: The maximum twin sum as an integer.
        """
        # Step 1: find the middle of the linked list using slow and fast pointers
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: reverse the second half of the linked list starting from slow
        prev = None
        current = slow
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt

        # prev now points to the head of the reversed second half
        # Step 3: traverse the first half and reversed second half simultaneously
        max_sum = 0
        first = head
        second = prev
        while second:
            # compute the twin sum of current pair
            twin_sum = first.val + second.val
            # update max_sum if necessary
            if twin_sum > max_sum:
                max_sum = twin_sum
            # move both pointers
            first = first.next
            second = second.next

        return max_sum
