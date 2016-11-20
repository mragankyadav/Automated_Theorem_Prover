import sys


class Solution(object):
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = len(s)
        arr = [[-2147 for i in range(l + 1)] for j in range(l + 1)]
        for i in range(len(s) + 1):
            arr[i][i] = 0

        for i in range(1, len(s) + 1):
            for j in range(1, len(s) + 1):
                gmin = sys.maxint
                if (j + i < len(s) + 1):
                    temps = s[j - 1:j + i]
                    # print temps
                    # print "first"+str(i)+" "+str(j)+" "
                    if (self.isPalin(temps)):
                        # print "inplain"
                        gmin = 0
                        arr[j][j + i] = gmin
                        continue
                    for k in range(j, j + i):
                        # print str(i)+" "+str(j)+" "+str(k)
                        # print str(arr[j][k])+" "+str(arr[k+1][j+i])
                        if (gmin > (arr[j][k] + arr[k + 1][j + i] + 1)):
                            gmin = arr[j][k] + arr[k + 1][j + i] + 1
                    arr[j][j + i] = gmin
        # print arr
        return arr[1][len(s)]

    def isPalin(self, s):
        if (len(s) == 0):
            return False
        elif (len(s) == 1):
            return True
        else:
            start = 0
            end = len(s) - 1
            while (start < end):
                if (s[start] != s[end]):
                    return False
                start += 1
                end -= 1
            return True

st="apjesgpsxoeiokmqmfgvjslcjukbqxpsobyhjpbgdfruqdkeiszrlmtwgfxyfostpqczidfljwfbbrflkgdvtytbgqalguewnhvvmcgxboycffopmtmhtfizxkmeftcucxpobxmelmjtuzigsxnncxpaibgpuijwhankxbplpyejxmrrjgeoevqozwdtgospohznkoyzocjlracchjqnggbfeebmuvbicbvmpuleywrpzwsihivnrwtxcukwplgtobhgxukwrdlszfaiqxwjvrgxnsveedxseeyeykarqnjrtlaliyudpacctzizcftjlunlgnfwcqqxcqikocqffsjyurzwysfjmswvhbrmshjuzsgpwyubtfbnwajuvrfhlccvfwhxfqthkcwhatktymgxostjlztwdxritygbrbibdgkezvzajizxasjnrcjwzdfvdnwwqeyumkamhzoqhnqjfzwzbixclcxqrtniznemxeahfozp"
obj=Solution()
print obj.minCut(st)