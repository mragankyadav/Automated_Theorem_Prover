from collections import deque
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        vertices=numCourses
        adj_list=[[] for i in range(0,vertices)]
        for i in range(0,len(prerequisites)):
            adj_list[(prerequisites[i])[1]].append((prerequisites[i])[0])
        #print adj_list

        indegrees=[0 for i in range(0,vertices)]

        for i in range(0,vertices):
            edges=adj_list[i]
            for j in range(0,len(edges)):
                indegrees[edges[j]]+=1

        #print "indegrees"+str(indegrees)
        q=deque()

        for i in range(0,vertices):
            if(indegrees[i]==0):
                q.append(i)

        #print q

        visited = [0 for i in range(0, vertices)]
        answer=[]
        while(len(q)>0):
            #print  q
            node=q.popleft()
            answer.append(node)
            #print node
            visited[node]=1
            edges= adj_list[node]
            for i in range(0,len(edges)):
                indegrees[edges[i]]-=1
                if(indegrees[edges[i]]==0):
                    q.append(edges[i])
            #print visited


        for i in range(0,vertices):
            if(visited[i]==0):
                return []
            else:
                continue
        return answer


obj=Solution()
print obj.canFinish(4, [[1,0],[2,0],[3,1],[3,2]])

