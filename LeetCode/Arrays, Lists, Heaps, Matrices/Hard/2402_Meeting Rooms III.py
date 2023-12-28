"""
https://leetcode.com/problems/meeting-rooms-iii/description/
"""


class Solution:
    # approach: priority queue, implemented using min heap
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # for rooms that are available
        unoccupied = [room for room in range(n)]
        # initializing empty list for rooms that'll be in use
        occupied = []
        # converting the unoccupied rooms list into a heap
        heapq.heapify(unoccupied)
        # initializing a list for the number of times each room gets booked
        booking_counts = [0] * n

        # sort meetings. ascending, according to first element (start time)
        srted = sorted(meetings, key=lambda x: x[0])
        for start, end_time in srted:
            # occupied[0] = first element in occupied. occupied[0][0] = end time of first element of occupied
            while occupied and occupied[0][0] <= start:
                # a room becomes available and we add it to the available rooms heap
                end, room = heapq.heappop(occupied)
                heapq.heappush(unoccupied, room)
            if unoccupied:
                # assign an available room from the heap to this meeting
                room = heapq.heappop(unoccupied)
                heapq.heappush(occupied, [end_time,
                                          room])  # adding the meeting to the occupied heap
            else:
                # if we got here, that means all rooms are occupied.
                # therefore, we find the room with the earliest end time. we use pop bc it's a minheap
                cur_end, room = heapq.heappop(occupied)
                new_end = cur_end + end_time - start  # update the rooms end time
                heapq.heappush(occupied, [new_end, room])
            booking_counts[room] += 1

        # now we'll find the room with the max booking counts
        max_bookings = max(booking_counts)
        most_booked = booking_counts.index(max_bookings)
        return most_booked
