class Solution(object):
    def mainfunc(self):
        nodes=int(raw_input())
        colors= map(int,raw_input().split(' '))
        adjlist=[set() for i in range(0,nodes+1)]
        for i in range(1,nodes):
            edge=map(int,raw_input().split(' '))
            adjlist[edge[0]].add(edge[1])
            adjlist[edge[1]].add(edge[0])
        self.dfstree(1,adjlist,colors,None)

    def dfstree(self, src, adjlist, colr, visited=None):

        if (visited==None):
            visited=set()
        visited.add(src)

        print adjlist[src]-visited
        for i in adjlist[src]-visited:
            self.dfstree(i ,adjlist,colr,visited)

obj=Solution()
obj.mainfunc()







