class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums=sorted(nums)


        ans=[]
        temp=[]

        for i in range(0,len(nums)):
            start = 0
            end = len(nums) - 1
            while(start<end and start!=i and end !=i):
                if(nums[start]+nums[end]>(-1*nums[i])):
                    end-=1
                elif(nums[start]+nums[end]<(-1*nums[i])):
                    start+=1
                elif nums[start]+nums[end]==(-1*nums[i]):
                    temp=[nums[start],nums[end],nums[i]]
                    start+=1
                    end-=1
                    if(len(ans)==0):
                        ans.append(temp)
                    else:
                        count=0
                        for j in ans:
                            if(set(j)!=set(temp)):
                                count+=1
                        if(count==len(ans)):
                            ans.append(temp)


        print ans

obj=Solution()
obj.threeSum([-1,-12,14,-6,4,-11,2,-7,13,-15,-1,11,-15,-15,13,-9,-11,-10,-7,-13,7,9,-13,-3,10,1,-5,12,11,-9,2,-4,-6,-7,5,5,-2,14,13,-12,14,-3,14,14,-11,5,12,-6,10,-9,-4,-6,-15,-9,-1,2,-1,9,-9,-5,-15,8,-2,-6,9,10,7,14,9,5,-13,9,-12,8,8,-8,-2,-2,1,-15,-4,5,-13,-4,3,1,5,-13,-13,11,-11,10,5,3,11,-9,-2,3,-10,-7,-6,14,9,-11,7,2,-4,13,7,5,13,-12,-13,7,-9,5,-7,11,-1,-12,8,3,13,-10,13,1,-4])


