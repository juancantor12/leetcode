"""
Given two strings ransomNote and magazine, return true if ransomNote can be constructed by 
using the letters from magazine and false otherwise.
Each letter in magazine can only be used once in ransomNote.

Example 1:
Input: ransomNote = "a", magazine = "b"
Output: false

Example 2:
Input: ransomNote = "aa", magazine = "ab"
Output: false

Example 3:
Input: ransomNote = "aa", magazine = "aab"
Output: true
"""
class Solution(object):
    """
    This solution works by creating a hashmap with a counter of the available words on magazine
    then, ransomNote is itrated and the counter is decreased when a letter should be used, if at
    any point the counter doesnt have enough letters, false is returned
    if the ransomNote is iterared completely without early termination, return true.
    """
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        counter = {}
        for c in magazine:
            if c not in counter:
                counter[c] = 1
            else:
                counter[c] += 1
        
        for c in ransomNote:
            if c in counter:
                counter[c] -= 1
                if counter[c] == 0:
                    del counter[c]
            else:
                return False
    
        return True


