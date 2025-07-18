"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 
Example 1:
Input: s = "()"
Output: true

Example 2:
Input: s = "()[]{}"
Output: true

Example 3:
Input: s = "(]"
Output: false

Example 4:
Input: s = "([])"
Output: true

Constraints:
1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""
class Solution:
    """

    """
    def isValid(self, s: str) -> bool:
        # opening_match is a dictionary with closing parentheses as keys and their equivalent opening one as values
        opening_match = {')':'(', '}':'{', ']':'['}
        stack = []
        for character in s:
            if character in opening_match: # If the current character is a closing parentheses
                # If there are parentheses on the stack, the last one must be the opening one for the current closing parentheses
                if len(stack) > 0 and stack[-1] == opening_match[character]:
                    # If that is the case, the current closing parentheses will cancel the last opening one in the stack, we can remove it
                    stack.pop()
                else:
                    # If the stack is empty or the last parentheses on it is not the opening of the current closing one, the string is invalid
                    return False
            else: # If the current character is not a closing parenthesis, it means is an opening one, just add it to the stack and continue
                stack.append(character)
        # If the stack is empty it means all opening parentheses were closed, if not, the sentence is not valid
        return True if len(stack) == 0 else False