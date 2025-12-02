"""
You are given a 2D integer array points, where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.

A horizontal trapezoid is a convex quadrilateral with at least one pair of horizontal sides (i.e. parallel to the x-axis). Two lines are parallel if and only if they have the same slope.

Return the number of unique horizontal trapezoids that can be formed by choosing any four distinct points from points.

Since the answer may be very large, return it modulo 109 + 7.
"""
counts = Counter(y for _, y in points).values()
        horizCnts = [comb(c,2) for c in counts]
        totalCnt = sum(horizCnts)
        squares = sum(map(mul, horizCnts, horizCnts))
        ans = (totalCnt * totalCnt//2) %1_000_000_007
        ans-= (squares//2) %1_000_000_007
        return ans %1_000_000_007