class Solution:
    """
    This solution works by iterating the array and "freeing" positions when the values are to be removed.
    when a value equal to val is found, it is "removed" by equaling it to "_" and its index added to a 
    "free_positions" list. If the values is different, k is increased, and if there are free positions 
    (there should be since the input is curated) the value will be moved to the first free position, 
    the current position will be "removed" and its index added to the free positions list, lastly, the just
    used position will be deleted, this last step can be consuming since deleting from an array shifts all
    remaining values so this can be improved. probably with a queue.
    """
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0 
        free_positions = []
        for i, v in enumerate(nums):
            if v == val:
                nums[i] = "_"
                free_positions += [i]
            else:
                k += 1
                if len(free_positions)>0:
                    nums[free_positions[0]] = v
                    nums[i] = "_"
                    free_positions += [i]
                    del free_positions[0]
        return k