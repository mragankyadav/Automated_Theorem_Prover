class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        k=len(nums)-1
        flag=0
        while(k>=0):
            for i in range(k,-1,-1):
                #print str(i)+"#"
                if(nums[k]>nums[i]):
                    temp=nums[k]
                    nums[k]=nums[i]
                    nums[i]=temp
                    print nums
                    nums[i+1:len(nums)]=sorted(nums[i+1:len(nums)])
                    k=-1
                    flag=1
                    break
                else:
                    continue
            k-=1
        if(flag==0):
            nums=sorted(nums)
        print nums
obj=Solution()
obj.nextPermutation([4,3,2,1])