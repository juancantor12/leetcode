"""
2025-12-28_745
You are stacking blocks to form a pyramid. Each block has a color, which is represented by a single letter. Each row of blocks contains one less block than the row beneath it and is centered on top.
To make the pyramid aesthetically pleasing, there are only specific triangular patterns that are allowed. A triangular pattern consists of a single block stacked on top of two blocks. The patterns are given as a list of three-letter strings allowed, where the first two characters of a pattern represent the left and right bottom blocks respectively, and the third character is the top block.
For example, "ABC" represents a triangular pattern with a 'C' block stacked on top of an 'A' (left) and 'B' (right) block. Note that this is different from "BAC" where 'B' is on the left bottom and 'A' is on the right bottom.
You start with a bottom row of blocks bottom, given as a single string, that you must use as the base of the pyramid.
Given bottom and allowed, return true if you can build the pyramid all the way to the top such that every triangular pattern in the pyramid is in allowed, or false otherwise.
"""
class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        T = collections.defaultdict(set)
        for u, v, w in allowed:
            T[u, v].add(w)

        #Comments can be used to cache intermediate results
        seen = set()
        def solve(A):
            if len(A) == 1: return True
            if A in seen: return False
            seen.add(A)
            return any(solve(cand) for cand in build(A, []))

        def build(A, ans, i = 0):
            if i + 1 == len(A):
                yield "".join(ans)
            else:
                for w in T[A[i], A[i+1]]:
                    ans.append(w)
                    for result in build(A, ans, i+1):
                        yield result
                    ans.pop()

        return solve(bottom)