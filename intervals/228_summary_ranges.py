"""
You are given a sorted unique integer array nums.
A range [a,b] is the set of all integers from a to b (inclusive).
Return the smallest sorted list of ranges that cover all the numbers in the array exactly.
That is, each element of nums is covered by exactly one of the ranges, 
and there is no integer x such that x is in one of the ranges but not in nums.

Each range [a,b] in the list should be output as:
"a->b" if a != b
"a" if a == b

Example 1:
Input: nums = [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]

Example 2:
Input: nums = [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
"""
class Solution:
    """
    This solution works by iterating the array once, creating a "start" point and then moving from this point onwards
    until the next value no longer is current + 1, here the interval is closed and the "start" of the new interval is set.
    """
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges = []  # List to hold the ranges
        i = 0  # Pointer to mark the start of an interval
        while i < len(nums):  # While the start hasn't surpased the lenght of the array
            start = nums[i]  # Initialize the start of the current range
            j = i+1  # And set a pointer to start traversing this interval
            # While this traversal pointer is less than the length and its value is the previous + 1
            while j < len(nums) and nums[j-1]+1 == nums[j]:
                j += 1  # Shift the traversal pointer to the right
            if start != nums[j-1]:  # When the interval finishes, if the start and current values are different
                ranges.append(f"{start}->{nums[j-1]}")  # add them to the ranges list
            else:
                ranges.append(f"{start}")  # and add the iterval only once if start and end are the same
            i = j  # when a interval is closed, move the start pointer to the place where the previous interval finished
        return ranges  # Lastly just return the intervals