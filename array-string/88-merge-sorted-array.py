"""
You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n,
representing the number of elements in nums1 and nums2 respectively.
Merge nums1 and nums2 into a single array sorted in non-decreasing order.
The final sorted array should not be returned by the function, but instead be stored inside the array nums1.
To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged,
and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Example 1:
Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
Output: [1,2,2,3,5,6]
Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
Example 2:
Input: nums1 = [1], m = 1, nums2 = [], n = 0
Output: [1]
Explanation: The arrays we are merging are [1] and [].
The result of the merge is [1].
Example 3:
Input: nums1 = [0], m = 0, nums2 = [1], n = 1
Output: [1]
Explanation: The arrays we are merging are [] and [1].
The result of the merge is [1].
Note that because m = 0, there are no elements in nums1. The 0 is only there to ensure the merge result can fit in nums1. 
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        This function works by iterating the first n numbers of both nums1 and nums2 from last to first
        and allocating them at the end of the target array (nums1), 3 pointers are used, one for each input array 
        (nums1 and nums2) and a third one to kep track of the position where the next number will be allocated.
        """
        p = m + n - 1 # Pointer for allocation, starts at the end of nums 1
        m -= 1 # last position of nums1
        n -= 1 # last position of nums2
        while n >= 0 and m >= 0: # While n and m are within range
            if nums2[n] > nums1[m]: # If the value on nums2 is higher
                nums1[p] = nums2[n] # allocate it at the current allocation position p
                n -= 1 # shift the nums2 pointer to the left
            else: # If the value of nums1 is greater or equal
                nums1[p] = nums1[m] # allocate it to the current p position on nums1
                m -= 1 # and shift nums1 pointer to the left
            p -= 1 # In any of the 2 cases, one number was allocated so we shift the o pointer to the left to
        while n >= 0: # Lastly, if m went to 0 but there are remaining values on nums2:
            nums1[p] = nums2[n] # allocate the values
            n -= 1 # and shift both, the nums2 pointer
            p -= 1 # and the nums1 allocation pointer
            
