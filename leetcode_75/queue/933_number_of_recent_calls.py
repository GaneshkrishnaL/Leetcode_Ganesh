"""
LeetCode Problem 933: Number of Recent Calls
https://leetcode.com/problems/number-of-recent-calls/

Problem Description:
You have a RecentCounter class which counts the number of recent requests within a certain time frame.
Implement the RecentCounter class:
- RecentCounter() Initializes the counter with zero recent requests.
- int ping(int t) Adds a new request at time t, where t represents some time in milliseconds,
  and returns the number of requests that has happened in the past 3000 milliseconds 
  (including the new request). Specifically, return the number of requests that have happened 
  in the inclusive range [t - 3000, t].

It is guaranteed that every call to ping uses a strictly larger value of t than the previous call.

Example:
Input: ["RecentCounter", "ping", "ping", "ping", "ping"]
       [[], [1], [100], [3001], [3002]]
Output: [null, 1, 2, 3, 3]

Time Complexity: O(1) for each ping operation (amortized)
Space Complexity: O(n) where n is the number of requests in the 3000ms window
"""

from collections import deque

class RecentCounter:
    """
    A class to count the number of recent requests within a 3000 millisecond time window.
    
    This implementation uses a queue (deque) to efficiently maintain only the requests
    that fall within the current time window, removing outdated requests automatically.
    """

    def __init__(self):
        """
        Initialize the RecentCounter with an empty queue.
        
        The queue will store timestamps of ping requests. We use a deque (double-ended queue)
        because it provides O(1) time complexity for both append and popleft operations,
        which are the primary operations we need for this problem.
        """
        self.q = deque()  # Initialize an empty deque to store request timestamps
        

    def ping(self, t: int) -> int:
        """
        Record a new request at time t and return the count of requests in [t-3000, t].
        
        Algorithm:
        1. Add the new timestamp t to the queue
        2. Remove all timestamps that are older than (t - 3000) from the front of the queue
        3. Return the size of the queue, which represents requests in the valid time window
        
        Args:
            t (int): The timestamp of the current request in milliseconds.
                     Guaranteed to be strictly increasing with each call.
        
        Returns:
            int: The number of requests that occurred in the time range [t-3000, t].
        
        Time Complexity: O(1) amortized - Each element is added once and removed once
        Space Complexity: O(W) where W is the maximum number of requests in a 3000ms window
        """
        # Step 1: Add the current timestamp to the end of the queue
        # This represents the new ping request at time t
        self.q.append(t)
        
        # Step 2: Remove outdated requests from the front of the queue
        # A request is outdated if it occurred more than 3000 milliseconds before time t
        # The condition checks if:
        # - The queue is not empty (self.q evaluates to True if not empty)
        # - The oldest timestamp (self.q[0]) is less than t-3000 (outside valid window)
        while self.q and self.q[0] < t - 3000:
            # Remove the oldest timestamp from the front of the queue
            # popleft() is O(1) operation for deque
            self.q.popleft()
        
        # Step 3: Return the count of valid requests
        # After removing outdated requests, all remaining requests in the queue
        # are within the [t-3000, t] time window
        return len(self.q)


# Usage Example:
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)
#
# Example execution:
# counter = RecentCounter()
# print(counter.ping(1))     # Returns 1: [1]
# print(counter.ping(100))   # Returns 2: [1, 100]
# print(counter.ping(3001))  # Returns 3: [1, 100, 3001]
# print(counter.ping(3002))  # Returns 3: [100, 3001, 3002] (1 is removed as it's < 3002-3000)
