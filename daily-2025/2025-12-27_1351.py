"""
2025-12-27_1351
Given a m x n matrix grid which is sorted in non-increasing order both row-wise and column-wise, return the number of negative numbers in grid.
"""
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        count = 0
        for row in grid:
            for i, val in enumerate(row):
                if val < 0:
                    count += len(row)-i
                    break
        return count