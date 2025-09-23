"""
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.
Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.

Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1, v2 = version1.split("."), version2.split(".")
        for i in range(max(len(v1), len(v2))):
            if i < len(v1) and i < len(v2):
                v1i, v2i = int(v1[i]), int(v2[i])
                if v1i == v2i: continue
                elif v1i > v2i: return 1
                else: return -1
            elif i < len(v1):
                if int(v1[i]) > 0: return 1
            else:
                if int(v2[i]) > 0: return -1
        return 0