"""
2025-12-22_2054
You are given a 0-indexed 2D integer array of events where events[i] = [startTimei, endTimei, valuei]. The ith event starts at startTimei and ends at endTimei, and if you attend this event, you will receive a value of valuei. You can choose at most two non-overlapping events to attend such that the sum of their values is maximized.
Return this maximum sum.
Note that the start time and end time is inclusive: that is, you cannot attend two events where one of them starts and the other ends at the same time. More specifically, if you attend an event with end time t, the next event must start at or after t + 1.
Editorial:
Create a min-heap (pq) to store pairs of event ending times and their corresponding values.
Sort the events array in ascending order by the start times of the events.
Initialize:
maxVal as 0 to store the maximum event value encountered so far.
maxSum as 0 to store the maximum sum of two non-overlapping event values.
Iterate through the events array:
For each event, while the heap is not empty and the ending time of the event at the top of the heap is less than the current event's start time:
Update maxVal to the maximum of its current value and the value from the top of the heap.
Remove the top element from the heap.
Update maxSum to the maximum of its current value and the sum of maxVal and the current event's value.
Push the current event's end time and value as a pair into the heap.
Return maxSum as the result after processing all events.
"""
class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Create a list to store the pair (end time, value) for events
        pq = []
        # Sort the events by their start time
        events.sort(key=lambda x: x[0])
        max_val = 0
        max_sum = 0
        for event in events:
            # Pop all valid events from the priority queue and take their maximum
            while pq and pq[0][0] < event[0]:
                max_val = max(max_val, pq[0][1])
                heapq.heappop(pq)
            # Calculate the maximum sum by adding the current event's value and the best previous event's value
            max_sum = max(max_sum, max_val + event[2])
            # Push the current event's end time and value into the heap
            heapq.heappush(pq, (event[1], event[2]))
        return max_sum
                