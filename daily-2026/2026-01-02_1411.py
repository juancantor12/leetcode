"""
2026-01-02_1411
You have a grid of size n x 3 and you want to paint each cell of the grid with exactly one of the three colors: Red, Yellow, or Green while making sure that no two adjacent cells have the same color (i.e., no two cells that share vertical or horizontal sides have the same color).
Given n the number of rows of the grid, return the number of ways you can paint this grid. As the answer may grow large, the answer must be computed modulo 109 + 7.
"""
class Solution(object):
    """
    The code counts how many ways to color an n × 3 grid using 3 colors.
    Adjacent cells (horizontal or vertical) cannot have the same color.
    Each row can only be colored in two valid pattern types.
    Pattern A (ABA): first and third cells have the same color.
    Pattern B (ABC): all three cells have different colors.
    A stores the number of ways ending with pattern ABA.
    B stores the number of ways ending with pattern ABC.
    For each new row, valid transitions update A and B.
    The final answer is A + B, modulo 1e9 + 7.
    """
    def numOfWays(self, n):
        MOD = 10**9 + 7
        A = B = 6
        for _ in range(2, n + 1):
            A, B = (2*A + 2*B) % MOD, (2*A + 3*B) % MOD
        return (A + B) % MOD