"""
You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].
A building is covered if there is at least one building in all four directions: left, right, above, and below.
Return the number of covered buildings.
"""
class Solution:
    def countCoveredBuildings(self, n: int, buildings: List[List[int]]) -> int:
        pinf = lambda: float('inf')
        ninf = lambda: float('-inf')
        max_x, min_x, max_y, min_y = defaultdict(ninf), defaultdict(pinf), defaultdict(ninf), defaultdict(pinf)
        for x, y in buildings:
            max_y[x] = max(max_y[x], y)
            min_y[x] = min(min_y[x], y)
            max_x[y] = max(max_x[y], x)
            min_x[y] = min(min_x[y], x)
        covered = 0
        for x, y in buildings:
            if (y > min_y[x] and y < max_y[x]) and (x > min_x[y] and x < max_x[y]):
                covered += 1
        return covered