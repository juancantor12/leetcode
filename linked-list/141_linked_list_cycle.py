"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer.
Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
Note that pos is not passed as a parameter.
Return true if there is a cycle in the linked list. Otherwise, return false.
"""
class Solution(object):
    """
    This solution works by implementing the "Floyd's Tortoise and Hare" algorithm, using a fast and a slow pointer.
    The idea is that if there is a cycle, the fast pointer will get to the slow one at some point, God knows why.
    """
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        slow, fast = head, head  # Define slow and fast pointers
        while fast and fast.next:  # While there are nodes to traverse
            slow = slow.next  # Move the slow pointer 1 position ahead
            fast = fast.next.next  # and move the fast pointer 2 positions
            if slow == fast: return True  # If at any point the fast pointer cactches up to the slow one, ther is a cycle
        return False  # If the fast pointer never catches up and the list is traversed, there is no cycle.