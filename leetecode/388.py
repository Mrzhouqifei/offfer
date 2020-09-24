class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\
        """
        input = input.split('\n')
        stack = []
        res = 0
        
        for x in input:
            t = x.count('\t')
            x = x[t:]
            while len(stack) > t:
                stack.pop()
            if '.' in x:
                length = len(x) + len(stack)
                for tmp in stack:
                    length += len(tmp)
                res = max(res, length)
            else:
                stack.append(x)
        return res
