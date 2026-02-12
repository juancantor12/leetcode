"""
2026-02-11_3713
We enumerate the left endpoint i of the substring and then enumerate the right endpoint j, where i≤j<n.
While extending the right endpoint, we maintain a frequency table cnt to count the occurrences of each character in the current substring.
For each substring [i,j], we iterate through cnt and check whether all characters that appear in the substring have the same frequency. If this condition is satisfied, we update the answer.
"""
class Solution:
    def longestBalanced(self, s: str) -> int:
        n = len(s)
        res = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(i, n):
                cnt[s[j]] += 1
                if len(set(cnt.values())) == 1:
                    res = max(res, j - i + 1)
        return res