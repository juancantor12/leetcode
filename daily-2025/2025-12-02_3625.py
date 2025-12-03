"""
You are given a 2D integer array points where points[i] = [xi, yi] represents the coordinates of the ith point on the Cartesian plane.
Return the number of unique trapezoids that can be formed by choosing any four distinct points from points.
A trapezoid is a convex quadrilateral with at least one pair of parallel sides. Two lines are parallel if and only if they have the same slope.
"""
class Solution:
    """
    Intuition
    Same idea on how we detect parallel side as for Q2. The 2 complications are:

    we work with multiple types of slopes and need to check every one by comparing points pairwise
    we may encounter rhombuses, which have 2 parallel groups of side and should still be counted only once
    To identify lines we will use k and b from the line equation y = k * x + b. We will also need to compute distance between points: length = sqrt((x1 - x2) ^ 2 + (y1 - y2) ^ 2). As we don't need the actual value, we will omit the sqrt part for simplicity.

    UPD-2: the term "rhombus" is incorrectly used in this post, the proper name is "parallelogram" as we don't necessarily need all 4 sides to have the same length. The only property we need is 2 pairs of parllel sides, as it's mentioned in both hints and other posts.

    Approach
    Prepare a list of processed points: seen_points.
    To avoid double counting you want to process each pair of points once. You can do the same with point indices e.g. first point in [0, n-1] and the second in [first+1, n-1] or [0, first-1].
    Prepare indices for seen types of lines
    Prepare indices for seen types of lines
    2.1. seen_parallel_lines - the number of all parallel lines for each slope K
    2.2. seen_same_lines - the number of parallel lines laying on the same line
    2.3. seen_parallel_line_sides - the number of parallel lines with the same length
    2.4. seen_same_line_sides - the number of parallel lines with the same length laying on the same line
    For each (x1, y1) point in points:
    3.1. Consider every previously seen point (x2, y2) from seen_points.
    3.2. Compute the line parameters: k and b.
    3.3. The hacky part: round these values up to 8 decimal points. I'm not quite sure in this part. The code fails without rounding and with round(val, 6) calls. I tried to use Fractional but it works ten times slower. Not sure if it can pass the time limit. There is most likely another way to handle these precision issues.
    3.4. Count the number all previously seen lines that can be used to form a trapezoid with the current line: these 2 lines should be parallel but shouldn't be collinear. That's exactly how we compute it: we use the total number of parallel lines and subtract all collinear ones.
    3.5. Add the line to the seen_parallel_lines and seen_same_lines indices.
    3.6. Track all rhombuses by counting all parallel lines with the same length and substract all collinear parallel lines with the same length.
    3.7. Add the line to the seen_parallel_line_sides and seen_same_line_sides indices.
    3.8. Add the (x1, y1) point to seen_points. (after the loop over (x2, y2) points)
    The final result is the number of potential trapezoids minus half of the rhombuses candidates we've found. We halve rhombuses as we counted them twice for each pair of a rhombus' parallel sides.
    """
    def countTrapezoids(self, points: List[List[int]]) -> int:
        """Solution copied."""
        seen_points = []
        # parallel => (k), same => (k, b)
        seen_parallel_lines = defaultdict(int)
        seen_same_lines = defaultdict(int)
        # + side_size added to each key: (k, side) & (k, b, side)
        seen_parallel_line_sides = defaultdict(int)
        seen_same_line_sides = defaultdict(int)
        
        result = 0
        rhombuses = 0
        for x1, y1 in points:
            for x2, y2 in seen_points:
                # y = k * x + b
                k = ((y1 - y2) / (x1 - x2)) if x1 - x2 != 0 else "inf"
                b = (y1 - k * x1) if k != "inf" else x1
                # floating point precision hack
                k = round(k, 8) if k != "inf" else k
                b = round(b, 8)

                slope_id = k
                line_id = (k, b)
                other_sides = seen_parallel_lines[slope_id] - seen_same_lines[line_id]
                result += other_sides

                seen_parallel_lines[slope_id] += 1
                seen_same_lines[line_id] += 1

                # handling rhombuses (counted twice)
                # props: same other side size (we will count it twice)
                dx, dy = abs(x1 - x2), abs(y1 - y2)
                side = dx * dx + dy * dy
                rhombuses += seen_parallel_line_sides[(k, side)] - seen_same_line_sides[(k, b, side)]

                seen_parallel_line_sides[(k, side)] += 1
                seen_same_line_sides[(k, b, side)] += 1
                
            seen_points.append((x1, y1))

        return result - rhombuses//2