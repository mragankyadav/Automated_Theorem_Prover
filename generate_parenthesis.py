class Solution(object):

    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans=[]
        str=""
        self.brackets(str,n,0,ans)
        print ans

    def brackets(self,str, open, close,ans):
        if(open==0 and close==0):
            ans.append(str)
        else:
            if(open>0):

                self.brackets(str+'(',open-1,close+1,ans)
            if(close>0):

                self.brackets(str+')',open,close-1,ans)

obj=Solution()
obj.generateParenthesis(3)