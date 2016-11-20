class Solution1(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if(len(strs)!=0):
            common=strs[0]
            for i in range(1,len(strs)):
                string = strs[i]
                for j in range(0,len(string)):
                    if(common[j]== string[j]):
                        continue
                    else:
                        common=common[0:j]
                        break

            print common
        else:
            print ""

list=['geeksforgeeks', 'geeks', 'geek', 'geezer']
obj= Solution1()
obj.longestCommonPrefix(list)
