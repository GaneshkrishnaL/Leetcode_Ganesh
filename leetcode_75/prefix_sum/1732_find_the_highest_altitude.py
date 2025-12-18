from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        """
        Given an array gain where gain[i] is the net gain in altitude between point i and i+1,
        compute the highest altitude the biker can reach.

        The biker starts at altitude 0. For each segment in gain, we update the current altitude
        by adding the gain and keep track of the maximum altitude encountered.
        
        :param gain: List[int] representing the altitude gain between consecutive points
        :return: int representing the highest altitude achieved
        """
        # Initialize the list of altitudes with the starting altitude of 0.
        altitudes = [0]
        # Iterate through each gain value, updating the current altitude.
        for change in gain:
            # The new altitude is the previous altitude plus the gain of this segment.
            altitudes.append(altitudes[-1] + change)
        # The highest altitude is simply the maximum value in the altitudes list.
        return max(altitudes)
