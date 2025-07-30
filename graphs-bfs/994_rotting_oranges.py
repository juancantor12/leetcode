"""
You are given an m x n grid where each cell can have one of three values:
0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
Return the minimum number of minutes that must elapse until no cell has a fresh orange. 
If this is impossible, return -1.
"""
class Solution:
    """
    This solution works by adding all initial rotten oranges to a queue, with the mark of the minute that has passed
    then, by BFS try to rot adjacent fresh oranges, adding them to the queue wiht the increase in the minute mark
    every time a orange gets rotten, we decrease the fresh orange count and try to inccrease the elapsed time
    with the current minute, when all rotten oranges have left the queue, if there remaining fresh counter drops to 0
    we return the max elapsed time, if not, return -1
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        fresh_oranges = 0  # counter for tracking how many fresh oranges are left
        rotten_oranges = deque()  # queue to add rotten oranges
        m = len(grid)  # grid dimentions
        n = len(grid[0])
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # directions to expand using BFS
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1:
                    fresh_oranges += 1  # increasing fresh orange count
                elif grid[row][col] == 2:
                    rotten_oranges.append((row, col, 0)) # adding rotten oranges to the queue at minute 0
        elapsed_minutes = 0  # this keeps track of the last elapsed minute, this is the return answer
        while rotten_oranges:  # start the bfs
            row, col, minute = rotten_oranges.popleft()
            for x, y in directions:  # explore directions
                next_row = row + x
                next_col = col + y
                # If the next cell is inbound and is a fresh orange
                if next_row >= 0 and next_row < m and next_col >= 0 and next_col < n and grid[next_row][next_col] == 1:
                    fresh_oranges -= 1  # decrease the fresh count
                    grid[next_row][next_col] = 2  # mark the orange as rooten
                    rotten_oranges.append((next_row, next_col, minute + 1))  # add it to the que with the increase in the minute mark
                    elapsed_minutes = max(elapsed_minutes, minute + 1)  # update the elapsed minutes, if this value would increase it.
        return elapsed_minutes if fresh_oranges == 0 else -1  # lastly return elapsed minutes if there are no fresh oranges left.