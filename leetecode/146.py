from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.q = deque()
        self.dict = dict()

    def get(self, key: int) -> int:
        if key in self.q:
            self.q.remove(key)
            self.q.append(key)
            return self.dict[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        self.dict[key] = value
        if key in self.q:
            self.q.remove(key)
        self.q.append(key)
        if len(self.q) > self.capacity:
            k = self.q.popleft()
            self.dict.pop(k)
        # print(self.q)



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)