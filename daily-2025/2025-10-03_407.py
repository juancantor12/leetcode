"""
Given an m x n integer matrix heightMap representing the height of each unit cell in a 2D elevation map, return the volume of water it can trap after raining.
"""
class Solution:
    def trapRainWater(self, heightMap: List[List[int]]) -> int:
        if not heightMap or len(heightMap) < 3 or len(heightMap[0]) < 3: return 0
        m, n = len(heightMap), len(heightMap[0])
        visited = [[False] * n for _ in range(m)]
        boundaries_heap = []
        # Add boundaries to the heap
        for i in range(m):
            heapq.heappush(boundaries_heap, (heightMap[i][0], i, 0)) # Tuple with height value, and coordinates
            heapq.heappush(boundaries_heap, (heightMap[i][n - 1], i, n - 1)) # Add the opposite side as well
            visited[i][0] = visited[i][n - 1] = True # and set them as visited
        for j in range(n):  # same for columns
            heapq.heappush(boundaries_heap, (heightMap[0][j], 0, j))
            heapq.heappush(boundaries_heap, (heightMap[m - 1][j], m - 1, j))
            visited[0][j] = visited[m - 1][j] = True
        
        trapped_water = 0
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        # Navigate heap untill all boundaries have been added
        while boundaries_heap:
            height, x, y = heapq.heappop(boundaries_heap)
            for dx, dy in directions:
                nx, ny = x + dx, y + dy # explore all directions
                if 0 <= nx < m and 0 <= ny < n and not visited[nx][ny]: # If direction is within bounds and cell is not visited.
                    # Trapped water around this cell will be the maximum value between 0 
                    # and the current cell height minus the height on the current neigbhor
                    trapped_water += max(0, height - heightMap[nx][ny])
                    # then we add either the neighbor height or the current cell if the neighbor height is lower, 
                    # the outer cell will be the boundary since it is higher and we are moving inwards.
                    heapq.heappush(boundaries_heap, (max(height, heightMap[nx][ny]), nx, ny)) # then we add the neighboor to the heap
                    visited[nx][ny] = True # and mark it as visited.
        # lastly just return
        return trapped_water