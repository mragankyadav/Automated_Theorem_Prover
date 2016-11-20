nums=[1,1,1,1,2,2,2,2,3,33]
class Solution(object):
    def removeDuplicates(self, nums,val):
        """
        :type nums: List[int]

        """
        length = len(nums)
        count = 0
        answer = []
        i = 0
        while (i < len(nums)):
            if(nums[i]==val):
                del nums[i]
            else:
                i+=1


        print nums

obj=Solution()
obj.removeDuplicates(nums,2)
