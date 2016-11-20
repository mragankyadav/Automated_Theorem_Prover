class Solution(object):
    def romanToInt(self, s):
        """

        :type s: str
        """

        double={'CM':900, 'CD':400, 'XC':90, 'XL':40, 'IX':9,'VI':6,'IV':4}
        single={'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5,'I':1 }
        s.upper()
        sum=0
        index=0
        while(index<len(s)):
            if( double.has_key(s[index:index+2])):
                sum+=double[s[index:index+2]]
                index+=2;

            elif (single.has_key(s[index])):
                sum+=single[s[index]]
                index+=1


        print str(sum)

object=Solution()
object.romanToInt("MMCMXCV")

        