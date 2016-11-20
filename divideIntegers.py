class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        rem=0
        ans=0
        while(dividend>divisor):
            divcopy=divisor
            count=0
            while(divcopy<=dividend):
                divcopy=divcopy<<1
                print str(dividend) + " " + str(divcopy)
                if(divcopy<=dividend):
                    count+=1
            divcopy=divcopy >> 1
            dividend-=divcopy
            print str(dividend)+" "+str(divcopy)
            ans+=2**count
        print ans
obj=Solution()
obj.divide(52,5)