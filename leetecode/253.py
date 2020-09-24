from queue import PriorityQueue
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:

        room, task = PriorityQueue(), PriorityQueue()
        room.put_nowait(0)
        for x in intervals:
            task.put_nowait((x[0], x[1]))
        while not task.empty():
            t = task.get_nowait()
            r = room.get_nowait()
            if t[0] >= r:
                r = t[1]
            else:
                room.put_nowait(t[1])
            room.put_nowait(r)
        return room.qsize()