"""
Approach 2: Sorting, Counting using Priority Queues
Intuition
In the preceding solution, the iteration over all N rooms occurs within the nested loop, resulting in an overall time complexity of O(M⋅N) for the for loop. To enhance efficiency we must explore avenues for optimization. We need to devise a method to obtain the next available room without the necessity of iterating over all N rooms. To do this we can maintain two crucial structures: unused_rooms and used_rooms. These structures are essentially priority queues or heaps, with unused_rooms representing available rooms sorted by room number, and used_rooms storing rooms in use along with the time they become available again.
We start by initialization of unused_rooms as a priority queue containing all room numbers and used_rooms as an empty priority queue.
unused_rooms is ordered in ascending order according to room numbers. This arrangement guarantees that when an element is popped from this, it returns the unused room with the lowest number. This is important to follow rule 1, which states that each meeting will take place in the unused room with the lowest number.
used_rooms is a priority queue that contains elements in the form of {room_availability_time, room_number}. Here, room_availability_time signifies the time at which this room becomes unused. This priority queue is ordered in ascending order based on both room_availability_time and room_number. This ensures that when an element is popped from it, the room returned is the one that becomes unused earliest. This assists in adhering to rules 2 and 3 while allocating a meeting to the room that becomes unused earliest when all rooms are currently in use.
Then we proceed to iterate through the meetings after sorting them based on their start times, adhering to the rule that meetings should be allocated based on their start times. Within this loop, a cascading series of decisions unfolds to handle various scenarios.
When iterating through meetings we first manage the release of rooms that have become unused. We iterate through used_rooms, popping rooms from the heap if their availability time is earlier than or equal to the start time of the current meeting. Released rooms are then pushed into unused_rooms.
Subsequently, we check if there are available rooms in unused_rooms. If so, the room with the lowest number is assigned to the current meeting. This follows the principle of allocating meetings to the unused room with the lowest number.
In the event that no rooms are available in unused_rooms, we resort to delaying the current meeting. We find the room with the earliest availability time (derived from the first item in used_rooms.) We then adjust the availability time of this room based on the duration of the delayed meeting, and push the room back into used_rooms. This ensures that meetings with earlier original start times are given priority when rooms become available and delayed meetings have the same duration as the original meeting.
Throughout this process, a crucial aspect is tracking of the count of meetings held in each room using the meeting_count array. This array is instrumental in determining the room that hosted the most meetings. After we have selected the room that hosts the meeting, we increment the count of meetings that occurred in that room.
Finally, we identify the room that held the most meetings and, in the case of a tie, select the room with the lowest number.
Algorithm
Create two priority queues, unused_rooms and used_rooms, representing the available and currently used rooms, respectively. Create an array meeting_count of size n to keep track of the number of meetings held in each room.
Use the heapify function to convert unused_rooms into a min heap, ensuring the room with the lowest number is at the top.
Iterate through the meetings sorted by start times.
While there are used rooms (used_rooms) and the first room's meeting has already concluded (meeting end time <= current meeting start time), remove the room from used_rooms and add it back to unused_rooms.
Check if there are available rooms (unused_rooms). If available, pop the room with the lowest number from unused_rooms and allocate the meeting to that room. Update used_rooms with the meeting end time and the room number.
If no available rooms, pop the room with the earliest availability time from used_rooms. Adjust the availability time for the room to accommodate the delayed meeting. Update used_rooms with the adjusted availability time and room number.
Increment the meeting count for the allocated room.
After processing all meetings, return the index of the room with the maximum meeting count using. If there are multiple rooms with the same maximum meeting count, return the room with the lowest index.
"""
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        unused_rooms, used_rooms = list(range(n)), []
        heapify(unused_rooms)
        meeting_count = [0] * n
        for start, end in sorted(meetings):
            while used_rooms and used_rooms[0][0] <= start:
                _, room = heappop(used_rooms)
                heappush(unused_rooms, room)
            if unused_rooms:
                room = heappop(unused_rooms)
                heappush(used_rooms, [end, room])
            else:
                room_availability_time, room = heappop(used_rooms)
                heappush(
                    used_rooms,
                    [room_availability_time + end - start, room]
                )
            meeting_count[room] += 1
        return meeting_count.index(max(meeting_count))