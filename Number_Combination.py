

globalMap = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}

class Solution(object):

    def func(self, stringVar, numbers, globalMap,answer):
        if (len(numbers) != 0):
            num = numbers[0]
            numbers=numbers[1:]
            alpha = globalMap[num]
            for i in alpha:
                self.func( stringVar + i, numbers,globalMap,answer)
        else:
            answer.append (stringVar)

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        stringVar = ""
        answer=[]
        if(len(digits)!=0):
            self.func(stringVar, digits, globalMap,answer)
            print answer
        else:
            print []






obj = Solution()
obj.letterCombinations('3')
