class Solution:
    def possibleBipartition(self, N: int, dislikes: List[List[int]]) -> bool:
        dis_len = len(dislikes)
        visited = [0] * dis_len
        a, b = set(), set()
        if not dislikes:
            return True
        a.add(dislikes[0][0])
        b.add(dislikes[0][1])
        visited[0] = 1
        while sum(visited) < dis_len:
            flag = False
            for i in range(1, dis_len):
                if not visited[i]:
                    x = dislikes[i]
                    if x[0] in a and x[1] not in a:
                        b.add(x[1])
                        visited[i] = 1
                        flag = True
                    elif x[0] in b and x[1] not in b:
                        a.add(x[1])
                        visited[i] = 1
                        flag = True
                    elif x[1] in a and x[0] not in a:
                        b.add(x[0])
                        visited[i] = 1
                        flag = True
                    elif x[1] in b and x[0] not in b:
                        a.add(x[0])
                        visited[i] = 1
                        flag = True
                    elif (x[0] in a and x[1] in a) or (x[0] in b and x[1] in b):
                        return False
            if not flag:
                for i in range(1, dis_len):
                    if not visited[i]:
                        x = dislikes[i]
                        a.add(x[0])
                        b.add(x[1])
                        break
        return True