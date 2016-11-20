starting_state = [[5, 6, 7], [4, 0, 8,], [3, 2, 1]]
goal_state=[[1,2,3],[8,0,4],[7,6,5]]
def h1(state,goal):
    score = 0
    for i in range(0, 3):
        for j in range(0, 3):
            if (state[i][j] != 0):
                if (state[i][j] != goal_state[i][j]):
                    score += 1
    print score

h1(starting_state,goal_state)