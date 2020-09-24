class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        edges_len = len(edges)
        nodes = [[] for _ in range(edges_len+1)]
        for edge in edges:
            nodes[edge[0]].append(edge[1])
            nodes[edge[1]].append(edge[0])

        def DFS(last, end, length):
            nonlocal max_length, last_node
            if length > max_length:
                max_length = length
                last_node = end
            for next in nodes[end]:
                if next != last:
                    DFS(end, next, length + 1)
        max_length, last_node = 0, 0
        DFS(-1, 0, 0)
        new_start = last_node
        max_length, last_node = 0, 0
        DFS(-1, new_start, 0)
        return max_length

