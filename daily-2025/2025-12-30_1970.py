"""
2025-12-30_1970
Intuition
The problem asks for the last day we can cross the grid.
We can observe a monotonic property here:

If it is possible to cross on day k, it is definitely possible to cross on any day before k (days 0 to k-1) because there is strictly less water.
If it is not possible to cross on day k, it is definitely not possible to cross on any day after k because there is strictly more water.
This "sorted" nature (possible → possible → ... → not possible) suggests that we can use Binary Search on the answer (the number of days).
For a specific day, we can simulate the grid state and verify reachability using a graph traversal algorithm like BFS (Breadth-First Search).

Approach
Binary Search Range: The possible answer ranges from 1 to row * col (or more tightly, 1 to len(cells)). We set left = 1 and right = row * col.
Check Function (canCross):
For a given day (the middle element of our binary search), we construct the grid.
We mark the cells listed in cells[:day] as water (1). All other cells are land (0).
We then attempt to find a path from the top row to the bottom row using
BFS.

We initialize a queue with all valid land cells in the first row (0, c).
We process the queue: for each cell, explore its 4 neighbors. If a neighbor is valid (within bounds, land, and unvisited), add it to the queue and mark it as visited.
If we reach any cell in the last row (row - 1), we return True.
If the queue becomes empty and we haven't reached the bottom, return False.
Binary Search Logic:

Calculate mid = (left + right) // 2.
If canCross(mid) is true, it means we can survive at least until this day. We store mid as a potential answer and try a later day: left = mid + 1.
If canCross(mid) is false, we need to try an earlier day: right = mid - 1.
Result: Return the largest day found.

Complexity
Time complexity: O(R⋅C⋅log(R⋅C))
The binary search performs O(log(R⋅C)) iterations.
In each iteration, we build the grid and run BFS, which takes O(R⋅C) time in the worst case (visiting every cell once).
Therefore, the total time complexity is O(R⋅C⋅log(R⋅C)).
Space complexity: O(R⋅C)
We use O(R⋅C) space to store the grid and the BFS queue.
"""
import collections
from typing import List

class Solution:
    def canCross(self, row, col, cells, day):
        # Create a grid initialized to 0 (land)
        grid = [[0] * col for _ in range(row)]
        queue = collections.deque()

        # Mark water cells for the current day
        # cells coordinates are 1-based, so convert to 0-based
        for r, c in cells[:day]:
            grid[r-1][c-1] = 1

        # Add all starting land cells from the top row to the queue
        # Note: The logic effectively runs BFS starting from available top-row cells
        for i in range(col):
            if not grid[0][i]:
                queue.append((0, i))
                grid[0][i] = -1  # Mark as visited
                           
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                
                for dr, dc in [(1,0), (0,1), (-1,0), (0,-1)]:
                    new_row, new_col = r + dr, c + dc
                    if 0 <= new_row < row and 0 <= new_col < col and grid[new_row][new_col] == 0:
                        grid[new_row][new_col] = -1  # Mark as visited
                        queue.append((new_row, new_col))
            
        return False

    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        left, right = 1, row * col
        ans = 0

        while left <= right:
            mid = (left + right) // 2

            if self.canCross(row, col, cells, mid):
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        
        return ans
            
            