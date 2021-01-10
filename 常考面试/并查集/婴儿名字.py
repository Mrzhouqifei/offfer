"""
面试题 17.07. 婴儿名字

"""


class UnionFind(object):
    def __init__(self, names):
        self.parent = {}
        for name in names:
            self.parent[name] = name

    def union(self, a, b):
        if a not in self.parent or b not in self.parent:
            return

        root_a = self.find_root(a)
        root_b = self.find_root(b)

        if root_a < root_b:
            self.parent[root_b] = self.parent[root_a]
        else:
            self.parent[root_a] = self.parent[root_b]

    def find_root(self, node):
        while node != self.parent[node]:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node


class Solution:
    def trulyMostPopular(self, names: List[str], synonyms: List[str]) -> List[str]:
        root_freq = {}
        # 频率map
        for name_freq in names:
            name, freq_str = name_freq.split('(')
            freq_str = freq_str[:-1]  # freq_str.strip(')')
            root_freq[name] = int(freq_str)

        # 初始化并查集
        uf = UnionFind(root_freq.keys())
        # 并操作
        for pair_str in synonyms:
            a, b = pair_str[1:-1].split(',')
            uf.union(a, b)

        # 查找生成结果
        result = []
        from collections import defaultdict
        union_freq = defaultdict(int)
        for name, freq in root_freq.items():
            union_freq[uf.find_root(name)] += freq
        for name, freq in union_freq.items():
            result.append('{}({})'.format(name, freq))
        return result