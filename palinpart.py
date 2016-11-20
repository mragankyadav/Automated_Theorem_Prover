class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        s = list(s)
        print s
        ans = self.recur(s, [], [])
        return ans

    def recur(self, s, temp, per):
        print s
        print temp
        print per
        print "#"
        if (len(s) <= 0):
            per.append(temp)
            return per
        st = ""
        for i in range(0, len(s)):
            st += s[i]
            if (self.isPalin(st)):
                per = self.recur(s[i + 1:], temp + [st], per)
        return per

    def isPalin(self, s):
        if (len(s) == 0):
            return False
        elif (len(s) == 1):
            return True
        else:
            start = 0
            end = len(s) - 1
            while (start < end):
                if s[start] != s[end]:
                    return False
                start+=1
                end-=1
            return True
obj=Solution()
obj.partition("aabb")