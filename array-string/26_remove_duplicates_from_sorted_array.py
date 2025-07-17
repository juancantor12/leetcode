"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element
appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements
in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements in the order they were presentin nums initially.
The remaining elements of nums are not important as well as the size of nums. Return k.

Custom Judge:
The judge will test your solution with the following code:
int[] nums = [...]; // Input array
int[] expectedNums = [...]; // The expected answer with correct length
int k = removeDuplicates(nums); // Calls your implementation
assert k == expectedNums.length;
for (int i = 0; i < k; i++) {
    assert nums[i] == expectedNums[i];
}
If all assertions pass, then your solution will be accepted.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
class Solution:
    """
    This solution works by iterating the array twice, in the first iteration all duplicate integers are replaced by None, leaving only one of each.
    In the second iteration, numbers are re-placed on available "free_positions", that is, positions that were empty or with "None".
    A pointer keeps track of what free positions have already been used by moving it 
    """
    def removeDuplicates(self, nums: List[int]) -> int:
        current_value = nums[0]  # Define current value
        i = 1  # Iteration starts at 1 since the first value will always be unique at that point
        n = len(nums) # To keep track of the array size on the while loop
        if n == 0: return 0  # Early stop for empty arrays
        if n == 1: return 1  # Early stop for arrays with just 1 element
        while i < n:  # Iterate the entire list for the first time
            if nums[i] == current_value:  # If the current position value is the same as the current value
                nums[i] = None  # Set it to None, to empty this position
            else:
                current_value = nums[i]  # If not, update the current value
            i += 1  # Bump the index to move forward
        # Second iteration: push or shift unique numbers to the beginning of the array
        free_positions = []  # Array to keep track of free positions or positiosn that have "None" as value
        i = 0  # Pointer to keep track of the array traversal
        j = 0  # Pointer to keep track of the free position to be used
        k = 0  # Counter to keep track of unique numbers
        while i < n:  # Second iteration
            if nums[i] == None:  # If the current position is free or has no value
                free_positions.append(i)  # Add it to free positions aray
            else:  # If the position has a number
                k += 1  # Bump the unique number counter
                if len(free_positions) > 0:  # If there are free positions
                    nums[free_positions[j]] = nums[i]  # Move the value to the first free position
                    j += 1  # Then bump the pointer of the free positions array since this position has already been used
                    nums[i] = None  # Set this position as empty or None since its value was moved to another positions
                    free_positions.append(i)  # Since this position became empty, add it to the free positions list
            i += 1  # Bump the pointer to iterate forward
        return k  # And lastly return the counter with the unique numbers count.
