import sys
import copy
import collections
import time
goalState=[[1,2,3],[8,0,4],[7,6,5]]
dfsGoalstate= [1,2,3,8,0,4,7,6,5]
startState=[]
#Medium [[2 ,8 ,1 ],[0, 4, 3 ],[7, 6, 5]]
#Hard [[5, 6, 7], [4, 0, 8,], [3, 2, 1]]

class dfsNode:
    # A special node structure for dfs implementation. Since DFS is highly unoptimal, it needed  a lot of different minor improvisations to
    #bring its  running time under a 10 minute limit. So various seprate functions have been made only for dfs and they all start with dfs_)
    def __init__(self,state,parent,movement,depth):
        self.state = state
        self.parent = parent
        self.movement = movement
        self.depth = depth

class Node:
    def __init__(self,starts=None,d=None,path=None,move=None,h=None):
        self.state=starts
        self.depth=d
        self.curPath=path
        self.operation=move
        self.hValue=h



    def generatechildren(self,parent,visited,h=None,totalNodes=None):
        children=[]
        xpos,ypos=None,None
        for i in range(0,3):
            for j in range(0,3):
                if(parent.state[i][j]==0 ):
                    xpos=i
                    ypos=j
                    break
            if xpos is not None:
                break

        if xpos is not 2:  # move down
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("DOWN")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1, tpath, "DOWN",h)
            child.state[xpos + 1][ypos], child.state[xpos][ypos] = child.state[xpos][ypos], child.state[xpos + 1][ypos]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if ypos is not 0 : #move left
            tpath=copy.deepcopy(parent.curPath)
            tpath.append("LEFT")
            child=Node(copy.deepcopy(parent.state),parent.depth+1,tpath,"LEFT",h)
            child.state[xpos][ypos-1],child.state[xpos][ypos]=child.state[xpos][ypos],child.state[xpos][ypos-1]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if ypos is not 2:  # move right
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("RIGHT")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1,tpath, "RIGHT",h)
            child.state[xpos][ypos+1], child.state[xpos][ ypos] = child.state[xpos][ypos], child.state[xpos][ypos+1]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        if xpos is not 0:  # move top
            tpath = copy.deepcopy(parent.curPath)
            tpath.append("UP")
            child = Node(copy.deepcopy(parent.state), parent.depth + 1,tpath, "TOP",h)
            child.state[xpos-1][ypos], child.state[xpos][ ypos] = child.state[xpos][ypos], child.state[xpos-1][ypos]
            if (self.toString(child.state) not in visited):
                children.append(child)
                totalNodes+=1

        return children,totalNodes

    def displayConfig(self,tlist):
        k=tlist[0]

    def toString(self,tempState):
        s=''
        for i in tempState:
            for j in i:
                s+=str(j)
        return s

    def heuristic_manhatten(self,state):
        score = 0
        goalx = [1, 0, 0, 0, 1, 2, 2, 2, 1]
        goaly = [1, 0, 1, 2, 2, 2, 1, 0, 0]
        for i in range(0, 3):
            for j in range(0,3):
                num=state[i][j]
                if(num!=0):
                    score += abs(i-goalx[num])+abs(j-goaly[num])
        return score

    def heuristic_displacedTiles(self,state):
        score=0
        for i in range(0,3):
            for j in range(0,3):
                if (state[i][j] != 0):
                    if(state[i][j]!=goalState[i][j]):
                        score+=1
        return score

    def dfs_create_node(self,state, parent, movement, depth):
        return dfsNode(state, parent, movement, depth)

    def dfs_move_up(self,node_state):
        # print node_state
        new_state = node_state[:]
        index = new_state.index(0)

        if index not in [0, 1, 2]:
            new_state[index] = new_state[index - 3]
            new_state[index - 3] = 0
            return new_state
        else:
            return None

    def dfs_move_down(self,node_state):
        # print node_state
        new_state = node_state[:]
        index = new_state.index(0)

        if index not in [6, 7, 8]:
            new_state[index] = new_state[index + 3]
            new_state[index + 3] = 0
            return new_state
        else:
            return None

    def dfs_move_left(self,node_state):
        # print node_state
        new_state = node_state[:]
        index = new_state.index(0)

        if index not in [0, 3, 6]:
            new_state[index] = new_state[index - 1]
            new_state[index - 1] = 0
            return new_state
        else:
            return None

    def dfs_move_right(self,node_state):
        # print node_state
        new_state = node_state[:]
        index = new_state.index(0)

        if index not in [2, 5, 8]:
            new_state[index] = new_state[index + 1]
            new_state[index + 1] = 0
            return new_state
        else:
            return None

    def expand_node(self,node):
        expanded_node_list = []

        if node.movement != "RIGHT":
            expanded_node_list.append(self.dfs_create_node(self.dfs_move_left(node.state), node, 'LEFT', node.depth + 1))
        if node.movement != "UP":
            expanded_node_list.append(self.dfs_create_node(self.dfs_move_down(node.state), node, 'DOWN', node.depth + 1))
        if node.movement != "DOWN":
            expanded_node_list.append(self.dfs_create_node(self.dfs_move_up(node.state), node, 'UP', node.depth + 1))
        if node.movement != "LEFT":
            expanded_node_list.append(self.dfs_create_node(self.dfs_move_right(node.state), node, 'RIGHT', node.depth + 1))

        expanded_node_list = [node for node in expanded_node_list if node.state != None]
        return expanded_node_list

    def dfs(self,start,goal):
        stime=time.time()
        timeFlag=0
        maxListSize=-sys.maxint-1
        totalnodes=0
        stack_nodes = []
        stack_nodes.append(self.dfs_create_node(start,None,None,0))
        if start == goal:
            return "No moves needed"
        visited = set()
        visited.add(''.join(str(i) for i in start))
        while len(stack_nodes) != 0:
            if(len(stack_nodes)>maxListSize):
                maxListSize=len(stack_nodes)
            if(time.time()-stime > (10*60)):
                timeFlag=1
                break
            node = stack_nodes.pop(0)
            if node.state == goal:
                sequence = []
                temp = node
                while temp.parent != None:
                    sequence.insert(0,temp.movement)
                    temp = temp.parent
                print "DFS Time "+str(time.time()-stime)
                print "Total Nodes Visited="+str(totalnodes)
                print "Max List Size="+str(maxListSize)
                return sequence
            else:
                nodes_expanded = self.expand_node(node)
                for n in nodes_expanded:
                    s = ''.join(str(i) for i in n.state)
                    if s not in visited:
                        totalnodes+=1
                        stack_nodes.insert(0,n)
                        visited.add(s)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalnodes)
            print "DFS terminated due to time out"
        return None


    def bfs(self):
        timeFlag=0
        maxListSize=-sys.maxint-1
        totalNodes=0
        start_time = time.time()
        q = collections.deque()
        visited = set()
        startNode = Node(startState, 1, [])
        q.append(startNode)
        flag = 0
        while (q):
            if len(q)>maxListSize:
                maxListSize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 10 * 60):
                timeFlag = 1
                break
            currentNode = q.popleft()
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            #print len(visited)
            if (currentNode.state == goalState):
                print "Moves="+str(len(currentNode.curPath))
                print currentNode.curPath
                flag = 1
                print ''
                print "Total Nodes Visited="+str(totalNodes)
                print "BFS Time"+ str(time.time()-start_time)
                print "Max List Size="+str(maxListSize)

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode, visited, None,totalNodes)
            q.extend(tchilds)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "BFS terminated due to TimeOut"

    def ids(self):
        timeFlag=0
        maxListsize=-sys.maxint-1
        totalNodes=0
        start_time = time.time()
        found_flag = 0
        flag=0
        depth = 1
        while(found_flag is not 1):
            stk = []
            startNode = Node(startState, 1, [])
            stk.append(startNode)
            #print "new started"
            #print depth
            while (stk):
                if len(stk)>maxListsize:
                    maxListsize=len(stk)
                temp_time = time.time()
                if (temp_time - start_time >= 1 * 60):
                    timeFlag = 1
                    break
                #print "stack" +str(len(stk))
                currentNode = stk.pop()

                stateString = self.toString(currentNode.state)
                if (currentNode.state == goalState):
                    print "Moves=" + str(len(currentNode.curPath))
                    print currentNode.curPath
                    flag = 1
                    found_flag=1
                    print ''
                    print "Total Nodes Visited="+str(totalNodes)
                    print "IDS Time"+ str(time.time()-start_time)
                    print "Max List Size="+str(maxListsize)
                if flag is 1:
                    break
                if (currentNode.depth+1 <= depth):
                    tchild,totalNodes=self.generatechildren(currentNode,set(),None,totalNodes)
                    stk.extend(tchild)
            depth+=1
            if timeFlag is 1:
                break
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "IDS terminated due to Timeout"


    def greedybfs_Manhatten(self):
        maxListsize = -sys.maxint - 1
        totalNodes=0
        timeFlag=0
        start_time = time.time()
        q=[]
        flag=0
        visited = set()
        startNode = Node(startState, 1, [],'',self.heuristic_manhatten(startState))
        q.append(startNode)
        while(q):
            if len(q)>maxListsize:
                maxListsize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 10 * 60):
                timeFlag = 1
                break
            q.sort(key=lambda x: x.hValue)
            currentNode= q.pop(0)
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            if (currentNode.state == goalState):
                print "Moves="+str(len(currentNode.curPath))
                print  str(currentNode.curPath)
                flag = 1
                print ''
                print "Total Nodes Visited=" + str(totalNodes)
                print "Greedy BFS with Manhatten Heuristic Time "+ str(time.time()-start_time)
                print "Max List Size="+str(maxListsize)

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode,visited,self.heuristic_manhatten(currentNode.state),totalNodes)
            q.extend(tchilds)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "Greedy BFS with Manhatten heuristic terminated due to TimeOut"

    def greedybfs_OutOFPlace(self):
        maxListsize = -sys.maxint - 1
        totalNodes=0
        timeFlag=0
        start_time = time.time()
        q=[]
        flag=0
        visited = set()
        startNode = Node(startState, 1, [],'',self.heuristic_displacedTiles(startState))
        q.append(startNode)
        while(q):
            if len(q)>maxListsize:
                maxListsize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 10 * 60):
                timeFlag = 1
                break
            q.sort(key=lambda x: x.hValue)
            currentNode= q.pop(0)
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            if (currentNode.state == goalState):
                print "Moves="+ str(len(currentNode.curPath))
                print str(currentNode.curPath)
                flag = 1
                print ''
                print "Total Nodes Visited="+str(totalNodes)
                print "Greedy BFS with Out of Place Heuristic Time "+ str(time.time()-start_time)
                print "Max List Size="+str(maxListsize)

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode,visited,self.heuristic_displacedTiles(currentNode.state),totalNodes)
            q.extend(tchilds)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "Greedy BFS with Out of Place heuristic terminated due to time out."

    def astar_Manhatten(self):
        maxListSize=-sys.maxint-1
        totalNodes=0
        timeFlag=0
        start_time = time.time()
        q = []
        flag = 0
        visited = set()
        startNode = Node(startState, 1, [], '', 1+self.heuristic_manhatten(startState))
        q.append(startNode)
        while (q):
            if len(q)>maxListSize:
                maxListSize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 10 * 60):
                timeFlag = 1
                break
            q.sort(key=lambda x: (x.hValue))
            currentNode = q.pop(0)
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            if (currentNode.state == goalState):
                print "Moves="+str(len(currentNode.curPath))
                print str(currentNode.curPath)
                flag = 1
                print ''
                print "Total Nodes Visited="+str(totalNodes)
                print "A* with Manhatten Heuristic Time "+ str(time.time()-start_time)
                print "Maximum List Size="+str(maxListSize)

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode, visited, currentNode.depth + self.heuristic_manhatten(currentNode.state),
                                  totalNodes)
            q.extend(tchilds)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "A* with Manhatten Heuristic terminated due to time out"

    def astar_OutOFPlace(self):
        maxListsize=-sys.maxint-1
        totalNodes=0
        timeFlag=1
        start_time = time.time()
        q=[]
        flag=0
        visited = set()
        startNode = Node(startState, 1, [],'',self.heuristic_displacedTiles(startState))
        q.append(startNode)
        while(q):
            if len(q)>maxListsize:
                maxListsize=len(q)
            temp_time = time.time()
            if (temp_time - start_time >= 10 * 60):
                timeFlag = 1
                break
            q.sort(key=lambda x: x.hValue)
            currentNode= q.pop(0)
            stateString = self.toString(currentNode.state)
            visited.add(stateString)
            if (currentNode.state == goalState):
                print "Moves="+str(len(currentNode.curPath))
                print str(currentNode.curPath)
                flag = 1
                print ''
                print "Total Nodes Visited=" + str(totalNodes)
                print "A* with Out of Place Heuristic Time"+ str(time.time()-start_time)
                print "Maximum List Size="+str(maxListsize)

            if flag is 1:
                break
            tchilds,totalNodes=self.generatechildren(currentNode,visited,currentNode.depth+self.heuristic_displacedTiles(currentNode.state),totalNodes)
            q.extend(tchilds)
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "A* with Out of Place Heuristic terminated due to time out."


    def idastar_Manhatten(self):
        maxDepthSize=-sys.maxint-1
        totalNodes=0
        timeFlag=0
        start_time = time.time()
        found_flag = 0
        flag = 0
        depth = 1
        while (found_flag is not 1):
            q = []
            flag = 0
            visited = set()
            startNode = Node(startState, 1, [], '', self.heuristic_manhatten(startState))
            q.append(startNode)
            while (q):
                temp_time = time.time()
                if (temp_time - start_time >= 10 * 60):
                    timeFlag = 1
                    break
                q.sort(key=lambda x: x.hValue)
                currentNode = q.pop(0)
                if(currentNode.depth>maxDepthSize):
                    maxDepthSize=currentNode.depth
                stateString = self.toString(currentNode.state)
                visited.add(stateString)
                if (currentNode.state == goalState):
                    print "Moves="+str(len(currentNode.curPath))
                    print str(currentNode.curPath)
                    flag = 1
                    found_flag=1
                    print ''
                    print "Total Nodes Visited=" + str(totalNodes)
                    print "IDA* with Manhatten Heuristic Time "+ str(time.time()-start_time)
                    print "Maximum Depth Visited="+str(maxDepthSize)

                if flag is 1:
                    break
                if (currentNode.depth+self.heuristic_manhatten(currentNode.state) + 1 <= depth):
                    tchilds,totalNodes=self.generatechildren(currentNode, visited, currentNode.depth+self.heuristic_manhatten(currentNode.state),totalNodes)
                    q.extend(tchilds)
            depth+=1
            if timeFlag is 1:
                break
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "IDA* with Manhatten Heuristic terminated due to time out "


    def idastar_displacedTiles(self):
        maxDepthSize=-sys.maxint-1
        totalNodes=0
        timeFlag=0
        start_time = time.time()
        found_flag = 0
        flag = 0
        depth = 1
        while (found_flag is not 1):
            q = []
            flag = 0
            visited = set()
            startNode = Node(startState, 1, [], '', self.heuristic_displacedTiles(startState))
            q.append(startNode)
            while (q):
                temp_time = time.time()
                if (temp_time - start_time >= 10 * 60):
                    timeFlag = 1
                    break
                q.sort(key=lambda x: x.hValue)
                currentNode = q.pop(0)
                if(currentNode.depth>maxDepthSize):
                    maxDepthSize=currentNode.depth
                stateString = self.toString(currentNode.state)
                visited.add(stateString)
                if (currentNode.state == goalState):
                    print "Moves="+str(len(currentNode.curPath))
                    print str(currentNode.curPath)
                    flag = 1
                    found_flag=1
                    print ''
                    print "Total Nodes Visited=" + str(totalNodes)
                    print "IDA* with Out of Place Heuristic Time "+ str(time.time()-start_time)
                    print "Maximum Depth Visited="+str(maxDepthSize)

                if flag is 1:
                    break
                if (currentNode.depth+self.heuristic_displacedTiles(currentNode.state) + 1 <= depth):
                    tchilds,totalNodes=self.generatechildren(currentNode, visited, currentNode.depth+self.heuristic_displacedTiles(currentNode.state),totalNodes)
                    q.extend(tchilds)
            depth+=1
            if timeFlag is 1:
                break
        if timeFlag is 1:
            print "Total Nodes Visited=" + str(totalNodes)
            print "IDA* with out of place tiles terminated due to timeout."



def mainfunction():

    print "Press the correct number for the required operation:"
    print "Press 1 for DFS "
    print "Press 2 for BFS"
    print "Press 3 for IDS"
    print "Press 4 for Greedy Best First Search using Manhatten Heuristic"
    print "Press 5 for Greedy Best First Search using Out of Place Tile Heuristic"
    print "Press 6 for A Star Search using Manhatten Heuristic"
    print "Press 7 for A Star Search using Out of Place Tile Heuristic"
    print "Press 8 for IDA Star Search using Manhatten Heuristic"
    print "Press 9 for IDA Star Search using Out of Place Heuristic"

    print ''
    functionCall= int(raw_input())


    #Parsing the input format to the required format for processing in python.
    print "Please input the  Start state in the form '(....)"
    inStartState=(raw_input())
    inStartState=inStartState.replace('(',' ( ')
    inStartState = inStartState.replace(')', ' ) ')
    for i in range(0,len(inStartState)):
        if inStartState[i] is '(':
            start=i+1
        elif inStartState[i]==')':
            end=i
    inStartState=inStartState[start:end]
    inStartState=map(int,inStartState.split())
    k=0
    for i in range(0,3):
        temp=[]
        for j in range(0,3):

            temp.append(inStartState[k])
            k+=1
        startState.append(temp)
    #Input parsed

    obj = Node()
    if functionCall is 1:
        result=obj.dfs(inStartState,dfsGoalstate)
        print "Moves="+str(len(result))
        print result
    elif functionCall is 2:
        obj.bfs()
    elif functionCall is 3:
        obj.ids()
    elif functionCall is 4:
        obj.greedybfs_Manhatten()
    elif functionCall is 5:
        obj.greedybfs_OutOFPlace()
    elif functionCall is 6:
        obj.astar_Manhatten()
    elif functionCall is 7:
        obj.astar_OutOFPlace()
    elif functionCall is 8:
        obj.idastar_Manhatten()
    elif functionCall is 9:
        obj.idastar_displacedTiles()






if __name__ == "__main__":
    mainfunction()