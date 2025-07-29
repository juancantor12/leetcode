"""
You are given an m x n matrix maze (0-indexed) with empty cells (represented as '.') and walls (represented as '+').
You are also given the entrance of the maze, where
entrance = [entrancerow, entrancecol] denotes the row and column of the cell you are initially standing at.
In one step, you can move one cell up, down, left, or right.
You cannot step into a cell with a wall, and you cannot step outside the maze.
Your goal is to find the nearest exit from the entrance.
An exit is defined as an empty cell that is at the border of the maze.
The entrance does not count as an exit.
Return the number of steps in the shortest path from the entrance to the nearest exit, or -1 if no such path exists.
"""
class Solution:
    """
    This solution works by exploring the matrix with a BFS algorithm, since BFS explores all paths at the same
    level on each step, whenever we get to an exit, it will be the nearest.
    """
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]  # Directions to move to: down, right, up and left.
        n, m = len(maze), len(maze[0])  # Dimentions of the maze
        q = deque()  # que to hold next cells to explore
        q.append((entrance[0], entrance[1], 0))  # start with the entrance and "0" steps
        while q:  # while there are cells to explore
            row, col, steps = q.popleft()  # get the current cell to explore
            if (
                (row == 0 or row == n-1) or (col == 0 or col == m-1)  # If the current cell is at the border
            ) and (row != entrance[0] or col != entrance[1]):  # and is not the entrance
                return steps  # this means is an exit, so we return the current amount of steps
            for direction in directions:  # iF is not an exit, we check each direction
                x = row + direction[0]  # by taking the current row and col
                y = col + direction[1]  # and adding the values of the direction we want to move to
                if x >= 0 and x < n and y >= 0 and y < m and maze[x][y] == ".":  # IF the new cell is inbounds and is empy (.)
                    maze[x][y] = "+"  # we mark is as a wall or as "explored" so the algorithm doesnt explore it further,
                    #  this replaces the "visited" set in a DFS search
                    q.append((x, y, steps+1))  # the next cell is added to the queue to explore its neighboors or check if its an exit.
        return -1  # if there was no early termination it means there is no exit and you are trapped foreeeeeeeeverrrrrr