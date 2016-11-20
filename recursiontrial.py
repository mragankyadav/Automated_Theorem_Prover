import copy
class Solution(object):
    def mainfunc(self):
        nodes=int(raw_input())
        colors= map(int,raw_input().split(' '))
        adjlist=[set() for i in range(0,nodes+1)]
        adjlistCopy=copy.deepcopy(adjlist)
        for i in range(1,nodes):
            edge=map(int,raw_input().split(' '))
            adjlist[edge[0]].add(edge[1])
            adjlist[edge[1]].add(edge[0])
            answer={}
        self.dfstree(1,adjlist,colors, answer, None)



    def dfstree(self, src, adjlist, colr, answer, visited=None):

        temp = set()
        if (visited==None):
            visited=set()


        visited.add(src)
        print src

        for i in adjlist[src]-visited:
           temp= temp|(self.dfstree(i ,adjlist,colr, answer, visited))
        temp= temp|set([colr[src-1]])
        print temp
        answer[src]=temp
        return temp



obj=Solution()
obj.mainfunc()







