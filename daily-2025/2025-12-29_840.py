"""
A 3 x 3 magic square is a 3 x 3 grid filled with distinct numbers from 1 to 9 such that each row, column, and both diagonals all have the same sum.
Given a row x col grid of integers, how many 3 x 3 magic square subgrids are there?
Note: while a magic square can only contain numbers from 1 to 9, grid may contain numbers up to 15.
"""
class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count, spiral, m, n = 0, [6,7,2,9,4,3,8], len(grid), len(grid[0])
        directions = {
            "r": [(1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)],
            "b": [(1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)],
            "l": [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)],
            "t": [(-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)],
        }
        for i in range(m):
            for j in range(n):
                # valid 5
                if grid[i][j] == 5 and i > 0 and i < m-1 and j > 0 and j < n-1:
                    # locate valid 1
                    for r, c, p in [(0, 1, "r"), (1, 0, "b"), (0, -1, "l"), (-1, 0, "t")]:
                        if grid[i+r][j+c] == 1:
                            # validate spirals
                            for h, (y, x) in enumerate(directions[p]):
                                if spiral[h] != grid[i+y][j+x]: break
                                elif h == 6: count += 1
                            for h, (y, x) in enumerate(directions[p]):
                                if spiral[6-h] != grid[i+y][j+x]: break
                                elif 6-h == 0: count += 1
                            break
        return count