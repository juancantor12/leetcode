"""
2026-02-726
Given two integers left and right, return the count of numbers in the inclusive range [left, right] having a prime number of set bits in their binary representation.

Recall that the number of set bits an integer has is the number of 1's present when written in binary.

For example, 21 written in binary is 10101, which has 3 set bits.
"""
class Solution:
    def countPrimeSetBits(self, left: int, right: int) -> int:
        max_1_value = len(bin(10**6))-3
        primes = []
        for i in range(2, max_1_value+1):
            prime = True
            for j in primes:
                if i % j == 0: 
                    prime = False
                    break
            if prime and i not in primes:
                primes.append(i)
        n = 0
        for i in range(left, right+1):
            if str(bin(i)).count("1") in primes:
                n += 1
        return n