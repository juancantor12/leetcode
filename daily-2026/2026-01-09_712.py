"""
2026-01-09_712
Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
Example 1:
Input: s1 = "sea", s2 = "eat"
Output: 231
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
Deleting "t" from "eat" adds 116 to the sum.
At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.

Intuition
This problem asks us to make two strings exactly the same by deleting characters.
Each deletion has a cost equal to the ASCII value of the deleted character, and our goal is to minimize the total cost.
A crucial shift in thinking makes this problem much easier:
Instead of focusing on which characters to delete, focus on which characters we keep.
If we choose a subsequence that appears in both strings:
All characters not in that subsequence must be deleted
The larger the ASCII sum of the kept subsequence, the smaller the total deletion cost
So the real objective becomes:
Find a common subsequence of s1 and s2 whose total ASCII value is as large as possible.
Once we know this value:
Let total_ascii be the sum of ASCII values of all characters in s1 and s2
Let keep be the ASCII sum of the best common subsequence
Then:
answer = total_ascii - 2 * keep
The factor 2 exists because the kept characters appear in both strings, so we avoid deleting them twice.
This turns the problem into a weighted Longest Common Subsequence (LCS) problem:
Normal LCS maximizes length
This problem maximizes ASCII value
Approach
We solve the problem using Dynamic Programming.
DP State Definition
Let dp[i][j] represent:
The maximum ASCII sum of a common subsequence between:
the first i characters of s1
the first j characters of s2
In simpler terms:
dp[i][j] answers
“What is the maximum ASCII value we can keep using prefixes s1 up to i and s2 up to j?”
This picture shows the populated matrix for "xabccde", "ace" test case.
love The Tech (4).png
Transitions
We iterate through both strings character by character.
Case 1: Characters Match
If s1[i - 1] equals s2[j - 1]:
We keep this character and increase the ASCII sum:
dp[i][j] = dp[i - 1][j - 1] + ASCII value of s1[i - 1]
Keeping matching characters is always optimal because they help both strings become equal.
Case 2: Characters Do Not Match
If s1[i - 1] does not equal s2[j - 1]:
We must skip one character:
Skip from s1 → dp[i - 1][j]
Skip from s2 → dp[i][j - 1]
We choose the option that preserves the higher ASCII sum:
dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
Base Cases
If either string is empty:
dp[0][j] = 0
dp[i][0] = 0
No common subsequence can exist when one string has length zero.
Final Answer Computation
After filling the DP table:
dp[n][m] stores the maximum ASCII sum of a common subsequence
Compute the total ASCII value of both strings
Subtract twice the kept value
minimum delete sum = total_ascii - 2 * dp[n][m]
Complexity
Time Complexity
O(n * m)
Each DP state is computed once.
Space Complexity
O(n * m)
The DP table stores results for all prefix combinations.
"""
class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        n, m = len(s1), len(s2)

        # dp[i][j] = maximum ASCII sum of common subsequence
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                if s1[i] == s2[j]:
                    dp[i + 1][j + 1] = dp[i][j] + ord(s1[i])
                else:
                    dp[i + 1][j + 1] = max(dp[i][j + 1], dp[i + 1][j])

        total_ascii = sum(ord(c) for c in s1) + sum(ord(c) for c in s2)
        return total_ascii - 2 * dp[n][m]