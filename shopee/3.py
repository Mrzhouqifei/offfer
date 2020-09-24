class LongestString:
    def getLongest(self, s, n):
          s.sort(key=lambda i:len(i),reverse=True)
          dicts = {k:True for k in s}
          for i in s:
            if self.getLongest_rec(i,dicts,True):
                return len(i)

    def getLongest_rec(self,key,dicts,value):
          if key in dicts and not value:
            return dicts[key]

          for i in range(len(key)):
            if self.getLongest_rec(key[:i],dicts,False) and self.getLongest_rec(key[i:],dicts,False):
                return True
          dicts[key] = False
          return False