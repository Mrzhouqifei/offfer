class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        graph = [[] for _ in range(n)]
        for s, e, w in flights:
            graph[s].append((e, w))

        from queue import PriorityQueue
        q = PriorityQueue()
        q.put_nowait((0, -1, src))  # cost, k, place

        best = {}  # end, k : price
        while not q.empty():
            price, k, end = q.get_nowait()
            if end == dst: return price

            for e, w in graph[end]:
                new_price = price + w
                if k < K and new_price < best.get((e, k+1), float('inf')):
                    best[e, k+1] = new_price
                    q.put_nowait((new_price, k+1, e))
        return -1