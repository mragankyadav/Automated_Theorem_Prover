import time

class Node:
    def __init__(self,state,parent,movement,depth):
        self.state = state
        self.parent = parent
        self.movement = movement
        self.depth = depth



def create_node(state, parent, movement,depth):
    return Node(state, parent, movement,depth)


def move_space_up(node_state):
   # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [0,1,2]:
        new_state[index] = new_state[index-3]
        new_state[index-3] = 0
        return new_state
    else :
        return None


def move_space_down(node_state):
   # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [6,7,8]:
        new_state[index] = new_state[index+3]
        new_state[index+3] = 0
        return new_state
    else :
        return None

def move_space_left(node_state):
    #print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [0,3,6]:
        new_state[index] = new_state[index-1]
        new_state[index-1] = 0
        return new_state
    else :
        return None

def move_space_right(node_state):
    #print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [2,5,8]:
        new_state[index] = new_state[index+1]
        new_state[index+1] = 0
        return new_state
    else :
        return None


def expand_node(node):
    expanded_node_list = []

    if node.movement != "RIGHT":
        expanded_node_list.append(create_node(move_space_left(node.state),node,'LEFT',node.depth+1))
    if node.movement != "UP":
        expanded_node_list.append(create_node(move_space_down(node.state),node,'DOWN',node.depth+1))
    if node.movement != "DOWN":
        expanded_node_list.append(create_node(move_space_up(node.state),node,'UP', node.depth+1))
    if node.movement != "LEFT":
        expanded_node_list.append(create_node(move_space_right(node.state),node,'RIGHT',node.depth+1))

    expanded_node_list = [node for node in expanded_node_list if node.state != None]
    return expanded_node_list




def dfs(start, goal):
    stime=time.time()
    stack_nodes = []
    stack_nodes.append(create_node(start,None,None,0))
    if start == goal:
        return "No moves needed"
    visited = set()
    visited.add(''.join(str(i) for i in start))
    while len(stack_nodes) != 0:
        node = stack_nodes.pop(0)
        if node.state == goal:
            sequence = []
            temp = node
            while temp.parent != None:
                sequence.insert(0,temp.movement)
                temp = temp.parent
            print time.time()-stime
            return sequence
        else:
            nodes_expanded = expand_node(node)
            for n in nodes_expanded:
                s = ''.join(str(i) for i in n.state)
                if s not in visited:
                    stack_nodes.insert(0,n)
                    visited.add(s)
    return None

startstate=[2 ,8 ,1 ,0 ,4 ,3 ,7 ,6 ,5]
    #[5 ,6 ,7 ,4 ,0 ,8 ,3 ,2 ,1]
goal=[1,2,3,8,0,4,7,6,5]
result=dfs(startstate,goal)
print len(result)
print result