class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if(n<=2):
            return 0
        arr=[]
        arr.append(0)
        arr.append(1)
        arr.append(2)
        count=0
        for i in range(3,n):
            arr.append(i)
        for i in range(3,len(arr)):
            if(arr[i]!=-1):
                count+=1
                for j in range(arr[i]*2,len(arr),arr[i]):
                    arr[j]=-1

        print count

obj=Solution()
obj.countPrimes(1500000)