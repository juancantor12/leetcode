"""
2025-12-23_3074
You are given an array apple of size n and an array capacity of size m.
There are n packs where the ith pack contains apple[i] apples. There are m boxes as well, and the ith box has a capacity of capacity[i] apples.
Return the minimum number of boxes you need to select to redistribute these n packs of apples into boxes.
Note that, apples from the same pack can be distributed into different boxes.
"""
class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        total_apples = sum(apple)
        sorted_boxes = sorted(capacity, reverse=True)
        ans = 0
        for cap in sorted_boxes:
            if total_apples > 0:
                total_apples -= cap
                ans += 1
            else:
                break
        return ans