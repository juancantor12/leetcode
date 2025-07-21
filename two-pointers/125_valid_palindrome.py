"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters
and removing all non-alphanumeric characters, it reads the same forward and backward.
Alphanumeric characters include letters and numbers.
Given a string s, return true if it is a palindrome, or false otherwise.

Example 1:
Input: s = "A man, a plan, a canal: Panama"
Output: true
Explanation: "amanaplanacanalpanama" is a palindrome.

Example 2:
Input: s = "race a car"
Output: false
Explanation: "raceacar" is not a palindrome.
"""
class Solution:
    """
    This solution works by movint two pointers from the outer ends of the string towards the center and comparing
    if the lowe case value at the current pointers is the same, if not, return false.
    To avoid non-alphanumeric values, an array with all valid characters is used to skip invalid chars.
    """
    def isPalindrome(self, s: str) -> bool:
        """ Define the alphanumeric array to validate chars againts."""
        alphanumeric = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
        i = 0  # left pointer
        j = len(s) - 1  # right pointer
        while i < j:  # while left hasn't reached or surpased right
            while s[i] not in alphanumeric and i < j:  # If The current left char is non-alphanumeric
                i += 1  #  shift the pointer to the left
            while s[j] not in alphanumeric and i < j:  # If The current right char is non-alphanumeric
                j -= 1  #  shift the pointer to the right
            if s[i].lower() != s[j].lower():  # When bot pointers point to valid chars, compare them
                return False  # Return false if they are not equal (not a valid palindrome)
            i += 1  # otherwise, shift both pointers inwards, left to the right
            j -= 1  # and right to the left
        return True  # If There wasnt an early stop, the phrase is a valid palindrome.