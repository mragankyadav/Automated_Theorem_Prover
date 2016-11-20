import sys

goal_state = [1, 2, 3, 8, 0, 4, 7, 6, 5]


class Node:
    def __init__(self, state, parent, movement, depth):
        self.state = state
        self.parent = parent
        self.movement = movement
        self.depth = depth


def create_node(state, parent, movement, depth):
    return Node(state, parent, movement, depth)


def move_space_up(node_state):
    # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [0, 1, 2]:
        new_state[index] = new_state[index - 3]
        new_state[index - 3] = 0
        return new_state
    else:
        return None


def move_space_down(node_state):
    # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [6, 7, 8]:
        new_state[index] = new_state[index + 3]
        new_state[index + 3] = 0
        return new_state
    else:
        return None


def move_space_left(node_state):
    # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [0, 3, 6]:
        new_state[index] = new_state[index - 1]
        new_state[index - 1] = 0
        return new_state
    else:
        return None


def move_space_right(node_state):
    # print node_state
    new_state = node_state[:]
    index = new_state.index(0)

    if index not in [2, 5, 8]:
        new_state[index] = new_state[index + 1]
        new_state[index + 1] = 0
        return new_state
    else:
        return None


def expand_node(node):
    expanded_node_list = []

    expanded_node_list.append(create_node(move_space_left(node.state), node, 'LEFT', node.depth + 1))
    expanded_node_list.append(create_node(move_space_down(node.state), node, 'DOWN', node.depth + 1))
    expanded_node_list.append(create_node(move_space_up(node.state), node, 'UP', node.depth + 1))
    expanded_node_list.append(create_node(move_space_right(node.state), node, 'RIGHT', node.depth + 1))

    expanded_node_list = [node for node in expanded_node_list if node.state != None]
    return expanded_node_list


def dfs(start, goal):
    stack_nodes = []
    stack_nodes.append(create_node(start, None, None, 0))
    if start == goal:
        return "No moves needed"
    visited = []
    visited.append(start)
    while len(stack_nodes) != 0:
        print len(visited)
        node = stack_nodes.pop(0)
        print node.state
        if node.state == goal:
            sequence = []
            temp = node
            while temp.parent != None:
                sequence.insert(0, temp.movement)
                temp = temp.parent
            return sequence
        else:
            nodes_expanded = expand_node(node)
            for n in nodes_expanded:
                if n.state not in visited:
                    stack_nodes.insert(0, n)
                    visited.append(n.state)
    return None


def ids(start, goal):
    iter_depth = -1
    while True:
        iter_depth += 1
        stack_nodes = []
        stack_nodes.append(create_node(start, None, None, 0))
        if start == goal:
            return "No moves needed"
        visited = []
        visited.append(start)
        while len(stack_nodes) != 0:
            node = stack_nodes.pop(0)

            print node.state
            if node.state == goal:
                sequence = []
                temp = node
                while temp.parent != None:
                    sequence.insert(0, temp.movement)
                    temp = temp.parent
                return sequence
            else:
                if node.depth < iter_depth:
                    nodes_expanded = expand_node(node)
                    for n in nodes_expanded:
                        if n.state not in visited:
                            stack_nodes.insert(0, n)
                            visited.append(n.state)


def bfs(start, goal):
    stack_nodes = []
    stack_nodes.append(create_node(start, None, None, 0))
    if start == goal:
        return "No moves needed"

    visited = []
    # visited.append(start)
    visited.append(''.join(str(i) for i in start))
    while len(stack_nodes) != 0:
        node = stack_nodes.pop(0)
        print node.state
        print len(visited)
        if node.state == goal:
            sequence = []
            temp = node
            while temp.parent != None:
                sequence.insert(0, temp.movement)
                temp = temp.parent
            return sequence
        else:
            nodes_expanded = expand_node(node)
            for n in nodes_expanded:
                s = ''.join(str(i) for i in n.state)
                if s not in visited:
                    stack_nodes.append(n)
                    visited.append(s)
    return None


def cmp_tiles(a, b):
    return (h1(a.state, goal_state) - h1(b.state, goal_state))


def cmp_man(a, b):
    return ((h2(a.state, goal_state)) - (h2(b.state, goal_state)))


def cmp_tiles_A(a, b):
    return ((a.depth + h1(a.state, goal_state)) - (b.depth + h1(b.state, goal_state)))


def cmp_man_A(a, b):
    return ((a.depth + h2(a.state, goal_state)) - (b.depth + h2(b.state, goal_state)))


def h1(state, goal):
    h_value = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            h_value += 1
    return h_value


def h2(state, goal):
    dist = 0
    for i in range(len(state)):
        idx = goal.index(state[i])
        xdist = abs(int(i % 3) - int(idx % 3))
        ydist = abs(int(i / 3) - int(idx / 3))
        dist += xdist + ydist
    return dist


def greedy(start, goal, heu="h1"):
    stack_nodes = []
    stack_nodes.append(create_node(start, None, None, 0))
    visited = []
    if start == goal:
        return "No moves needed"
    while len(stack_nodes) != 0:
        if heu == "h1":
            stack_nodes.sort(cmp_tiles)
        else:
            stack_nodes.sort(cmp_man)
        node = stack_nodes.pop(0)
        visited.append(node.state)
        if node.state == goal:
            sequence = []
            temp = node
            while temp.parent != None:
                sequence.insert(0, temp.movement)
                temp = temp.parent
            return sequence
        else:
            nodes_expanded = expand_node(node)
            for n in nodes_expanded:
                if n.state not in visited:
                    stack_nodes.append(n)
    return None


def a_star(start, goal, heu="h1"):
    stack_nodes = []
    stack_nodes.append(create_node(start, None, None, 0))
    visited = []
    if start == goal:
        return "No moves needed"

    while len(stack_nodes) != 0:
        if heu == "h1":
            stack_nodes.sort(cmp_tiles_A)
        else:
            stack_nodes.sort(cmp_man_A)
        node = stack_nodes.pop(0)
        print node.state
        visited.append(node.state)
        if node.state == goal:
            sequence = []
            temp = node
            while temp.parent != None:
                sequence.insert(0, temp.movement)
                temp = temp.parent
            return sequence
        else:
            nodes_expanded = expand_node(node)
            for n in nodes_expanded:
                if n.state in visited:
                    continue
                flag = False
                for x in stack_nodes:
                    if x.state == n.state:
                        if x.depth > n.depth:
                            stack_nodes.remove(x)
                            stack_nodes.append(n)
                        flag = True
                        break

                if flag == False:
                    stack_nodes.append(n)

                '''
                if n in stack_nodes:
                    index = stack_nodes.index(n)
                    if n.depth < stack_nodes[index].depth:
                        stack_nodes.remove(stack_nodes[index])
                        stack_nodes.append(n)
                else :
                    stack_nodes.append(n)
                    '''
    return None


def main():
    state_given = raw_input()
    starting_state = map(int, state_given[2:19:1].split())
    result = bfs(starting_state, goal_state)
    if result == None:
        print "No Solution Found"
    else:
        print result


if __name__ == "__main__":
    main()
