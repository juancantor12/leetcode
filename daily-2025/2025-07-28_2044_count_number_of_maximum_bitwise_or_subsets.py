"""
Given an integer array nums, find the maximum possible bitwise OR of a subset of nums and return the 
number of different non-empty subsets with the maximum bitwise OR.
An array a is a subset of an array b if a can be obtained from b by deleting some (possibly zero) elements of b.
Two subsets are considered different if the indices of the elements chosen are different.
The bitwise OR of an array a is equal to a[0] OR a[1] OR ... OR a[a.length - 1] (0-indexed).

Example 1:
Input: nums = [3,1]
Output: 2
Explanation: The maximum possible bitwise OR of a subset is 3. There are 2 subsets with a bitwise OR of 3:
- [3]
- [3,1]

Example 2:
Input: nums = [2,2,2]
Output: 7
Explanation: All non-empty subsets of [2,2,2] have a bitwise OR of 2. There are 23 - 1 = 7 total subsets.

Example 3:
Input: nums = [3,2,1,5]
Output: 6
Explanation: The maximum possible bitwise OR of a subset is 7. There are 6 subsets with a bitwise OR of 7:
- [3,5]
- [3,1,5]
- [3,2,5]
- [3,2,1,5]
- [2,5]
- [2,1,5]
"""
class Solution:
    """
    This solution works by pre-calculating the maximum OR of the entire list, then, traversing all posible subsets
    of nums using a DFS approach where at each step, there are 2 subset choices, to include the next number or not to.
    whenever the DFS algorithm reaches the end of the array (incomplete subsets will never reach max), 
    if the accumulated OR value is equal to the maximum, the response value is increased by 1 and the dfs call ends.
    If the dfs hasn't reached the end of the array, two options
    are explored, one where the current nums value is factored with the current OR (including the item in the subset)
    and one where it isnt, excluding it.

    """
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0  # calculate the entire array OR
        for n in nums:
            max_or |= n

        maximum_or_subsets = 0
        def dfs(index, current_or):
            nonlocal maximum_or_subsets, max_or
            if index == len(nums):  # if we reached the end of the array
                if current_or == max_or:  # if the current accumulated OR is equal to the max
                    maximum_or_subsets += 1  # "add" this subset to the list of subsets that have max or
                return  # and finisht this dfs path.
            
            # call DFS skipping the current number
            dfs(index+1, current_or)
            # call DFS including current number
            dfs(index+1, current_or | nums[i])

        dfs(0, 0)  # kickstart the dfs
        return maximum_or_subsets  # and return the counter