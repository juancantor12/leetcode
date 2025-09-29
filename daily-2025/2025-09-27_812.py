"""
Given an array of points on the X-Y plane points where points[i] = [xi, yi], return the area of the largest triangle that can be formed by any three different points.
Answers within 10-5 of the actual answer will be accepted.

"""
class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        n = len(points)
        res = float('-inf')
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    x1, y1 = points[i]
                    x2, y2 = points[j]
                    x3, y3 = points[k]
                    area = 0.5*abs(x1*(y2-y3) + x2*(y3-y1) + x3*(y1-y2))
                    res = max(res, area)
        return res