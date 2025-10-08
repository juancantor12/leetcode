"""
** this description is unintelligible **

Your country has an infinite number of lakes. Initially, all the lakes are empty, but when it rains over the nth lake, the nth lake becomes full of water. If it rains over a lake that is full of water, there will be a flood. Your goal is to avoid floods in any lake.
Given an integer array rains where:
rains[i] > 0 means there will be rains over the rains[i] lake.
rains[i] == 0 means there are no rains this day and you can choose one lake this day and dry it.
Return an array ans where:
ans.length == rains.length
ans[i] == -1 if rains[i] > 0.
ans[i] is the lake you choose to dry in the ith day if rains[i] == 0.
If there are multiple valid answers return any of them. If it is impossible to avoid flood return an empty array.
Notice that if you chose to dry a full lake, it becomes empty, but if you chose to dry an empty lake, nothing changes.
"""

from bisect import bisect_right
from sortedcontainers import SortedList

class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        res = [-1]*len(rains) # Return array with -1 on days where it rains and the lake to dry if its a dry day
        full_lakes = {} # To keep track of what lakes are filled
        dry_days = SortedList()  # To keep track of dry days
        for day, lake in enumerate(rains):  # Iterate over the days and the rained on lakes
            if lake == 0:  # If the lake is 0 it means no rain
                dry_days.add(day)  # so this day can be added do the dry days sorted list
                res[day] = 1 # This is a dummy lake for when no lake needs to be dried, leetcode will take any number but 0 or -1
            elif lake not in full_lakes: # if it rains and the lake is empty, fill it by storing the index on the day it rained
                full_lakes[lake] = day
            else: # Else, the lake is on full_lakes, meaning it will flood
                j = dry_days.bisect_right(full_lakes[lake]) # get the index of a dry day after it last rained:
                if j == len(dry_days): # if this day index is out of the list, the lake cannot be dried and it will flood
                    return []
                res[dry_days[j]] = lake # Otherwise, we mark that we dry this lake on that day
                dry_days.pop(j) # no clue why we pop from dry_days
                full_lakes[lake] = day # no clue also
        return res # this list holds now the days where lakes should be dried