"""
面试题 17.07. 婴儿名字

每年，政府都会公布一万个最常见的婴儿名字和它们出现的频率，也就是同名婴儿的数量。有些名字有多种拼法，
例如，John 和 Jon 本质上是相同的名字，但被当成了两个名字公布出来。给定两个列表，一个是名字及对应的频率，
另一个是本质相同的名字对。设计一个算法打印出每个真实名字的实际频率。注意，如果 John 和 Jon 是相同的，
并且 Jon 和 Johnny 相同，则 John 与 Johnny 也相同，即它们有传递和对称性。

在结果列表中，选择 字典序最小 的名字作为真实名字。

示例：
输入：names = ["John(15)","Jon(12)","Chris(13)","Kris(4)","Christopher(19)"],
     synonyms = ["(Jon,John)","(John,Johnny)","(Chris,Kris)","(Chris,Christopher)"]
输出：["John(27)","Chris(36)"]

"""


class UnionFind(object):
    def __init__(self, names):  # 初始化并查集为自身
        self.parent = {}
        for name in names:
            self.parent[name] = name

    def union(self, a, b):  # 并
        if a not in self.parent or b not in self.parent:
            return

        root_a = self.find_root(a)
        root_b = self.find_root(b)

        if root_a < root_b:  # （根据字典序大小）进行parent并操作
            self.parent[root_b] = self.parent[root_a]
        else:
            self.parent[root_a] = self.parent[root_b]

    def find_root(self, node):  # 查
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