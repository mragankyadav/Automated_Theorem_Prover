class Solution(object):
    def lengthOfLIS(self, nums):

        if(len(nums)!=0):
            ans=[1]
            for i in range(1,len(nums)):
                maximum=1
                for j in range(0,i):
                    if(nums[i]>nums[j] and 1+ans[j]>maximum):
                        maximum=1+ans[j]

                ans.append(maximum)
            print max(ans)
        else:
            print 0

obj=Solution()
obj.lengthOfLIS([1,3,6,7,9,4,10,5,6])












