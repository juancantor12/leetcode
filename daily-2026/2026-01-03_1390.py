"""
2026-01-03_1390
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.
Intuition
We need to consider only those numbers that have exactly 4 divisors.
Instead of finding all divisors up to n, we observe:
Divisors come in pairs: (i, n/i)
We only need to check divisors up to √n
While counting divisors:
If divisor count becomes more than 4, we stop early (optimization).
If a number has exactly 4 divisors, we add the sum of those divisors to the final answer.
Approach
For each number n in the array:
Initialize:
cnt = 0 → counts number of divisors
s = 0 → sum of divisors
Loop from i = 1 to √n:
If i divides n:
Let j = n / i
If i == j → perfect square → count once
Else → count both i and j
Add divisor(s) to sum
If divisor count exceeds 4 → break early
After loop:
If cnt == 4, add s to total sum
eturn the total sum
"""
class Solution:
    def sumFourDivisors(self, nums):
        total = 0
        for n in nums:
            cnt = 0
            s = 0
            root = int(n ** 0.5)
            for i in range(1, root + 1):
                if n % i == 0:
                    j = n // i
                    if i == j:
                        cnt += 1
                        s += i
                    else:
                        cnt += 2
                        s += i + j
                    if cnt > 4:
                        break
            if cnt == 4:
                total += s
        return total