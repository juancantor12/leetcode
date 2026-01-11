"""
2026-01-11_85
Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
Approach
I create an array heights with size = number of columns.
I iterate row by row.
For each cell:
If it is '1', I increase the height.
If it is '0', I reset the height to 0.
After updating heights for a row, I calculate the largest rectangle area in a histogram using a monotonic stack.
I repeat this for all rows and store the maximum area.
"""
class Solution:
    def maximalRectangle(self, matrix):
        if not matrix:
            return 0

        cols = len(matrix[0])
        heights = [0] * cols
        max_area = 0

        def largestRectangleArea(heights):
            stack = []
            max_area = 0
            heights.append(0)

            for i in range(len(heights)):
                while stack and heights[stack[-1]] > heights[i]:
                    h = heights[stack.pop()]
                    w = i if not stack else i - stack[-1] - 1
                    max_area = max(max_area, h * w)
                stack.append(i)

            heights.pop()
            return max_area

        for row in matrix:
            for j in range(cols):
                heights[j] = heights[j] + 1 if row[j] == '1' else 0
            max_area = max(max_area, largestRectangleArea(heights))

        return max_area