"""
You have a convex n-sided polygon where each vertex has an integer value. You are given an integer array values where values[i] is the value of the ith vertex in clockwise order.
Polygon triangulation is a process where you divide a polygon into a set of triangles and the vertices of each triangle must also be vertices of the original polygon. Note that no other shapes other than triangles are allowed in the division. This process will result in n - 2 triangles.
You will triangulate the polygon. For each triangle, the weight of that triangle is the product of the values at its vertices. The total score of the triangulation is the sum of these weights over all n - 2 triangles.
Return the minimum possible score that you can achieve with some triangulation of the polygon.

Example 1:
Input: values = [1,2,3]
Output: 6
Explanation: The polygon is already triangulated, and the score of the only triangle is 6.

Example 2:
Input: values = [3,7,4,5]
Output: 144
Explanation: There are two triangulations, with possible scores: 3*7*5 + 4*5*7 = 245, or 3*4*5 + 3*4*7 = 144.
The minimum score is 144.

Example 3:
Input: values = [1,3,1,4,1,5]
Output: 13
Explanation: The minimum score triangulation is 1*1*3 + 1*1*4 + 1*1*5 + 1*1*1 = 13.
"""
class Solution:
    def __init__(self):
        self.dp = [[0] * 50 for _ in range(50)] # Initialize a 2D DP matrix 50x50
        
    def minScoreTriangulation(self, values, i=0, j=0, res=0):
        if j == 0:
            j = len(values) - 1  # If j is not defined yet, it should be fixed at the last vertex
        if self.dp[i][j] != 0:  # If this triangulaiton was already calculated
            return self.dp[i][j]  # Return it.
        for k in range(i + 1, j): # If not, calculate the current calculation
            # Pick the minimum triangulation product bewtween:
            res = min( 
                    res if res != 0 else float('inf'), # The current res if different from 0
                    # The sum of the triangulation from the left polygon plus the curren triangle plus the right polygon
                    self.minScoreTriangulation(values, i, k) + values[i] * values[k] * values[j] + self.minScoreTriangulation(values, k, j)
                )
        self.dp[i][j] = res # update DP matrix for the position i, j
        return self.dp[i][j]   # return the value for this triangulation.