import search
import random
import math


ids = ["935885178", "203609177"]


def manhattan_real_distance(packman_row, packman_col, row, col):
    #print(packman_row,'-', row,'|',packman_col, '-', col)
    return abs(packman_row - row) + abs(packman_col - col)


def closest_dot_distance(state, pacman_row, packman_col):

    shortest_dist = float('Inf')
    maximum_dist = 0
    dot_col = 0

    for row in range(len(state)):
        for col in range(len(state[row])):
            if state[row][col] == 11:
                #print(row,col)
                dist = manhattan_real_distance(pacman_row, packman_col, row, col)
                if dist<shortest_dist:
                    shortest_dist=dist
                if dist>maximum_dist:
                    maximum_dist = dist
    #print(shortest_dist)
    #print(state)
    if shortest_dist == float('Inf'):
        shortest_dist=0
    return  shortest_dist, maximum_dist

class PacmanProblem(search.Problem):

    def find_row_col(self, state, agent):
        a_row = None
        a_col = None
        for row in state:
            if agent in row:
                a_row = state.index(row)
                a_col = row.index(agent)
        return a_row, a_col

    def point_sum(self, state):
        counter = 0
        for row in state:
            for col in row:
                if col in (11, 71, 51, 41, 31, 21):
                    counter = counter + 1
        return counter

    """This class implements a spaceship problem"""

    def __init__(self, initial):
        """Don't forget to set the goal or implement the goal test
        You should change the initial to your own representation"""


        search.Problem.__init__(self, initial)


    def actions(self, state):
        """Return the actions that can be executed in the given
        state. The result would typically be a tuple, but if there are
        many actions, consider yielding them one at a time in an
        iterator, rather than building them all at once."""
        allowed_lst = []
        packman_row, packman_col = self.find_row_col(state, 66)
        if packman_row == None:
            return tuple(allowed_lst)
        allowed_field = (10, 11)
        if state[packman_row + 1][packman_col] in allowed_field:
            allowed_lst.append("D")
        if state[packman_row - 1][packman_col] in allowed_field:
            allowed_lst.append("U")
        if state[packman_row][packman_col + 1] in allowed_field:
            allowed_lst.append("R")
        if state[packman_row][packman_col - 1] in allowed_field:
            allowed_lst.append("L")
        #print(allowed_lst)
        return tuple(allowed_lst)

    def manhattan_distance(self, state, ghost_row, ghost_col, packman_row, packman_col):
        distance = {}
        distance["R"] = abs(packman_row - ghost_row) + abs(packman_col - (ghost_col + 1))
        distance["L"] = abs(packman_row - ghost_row) + abs(packman_col - (ghost_col - 1))
        distance["D"] = abs(packman_row - (ghost_row + 1)) + abs(packman_col - ghost_col)
        distance["U"] = abs(packman_row - (ghost_row - 1)) + abs(packman_col - ghost_col)
        smallest = min(distance.items(), key=lambda x: x[1])[0]
        for i in range(4):
            if distance["R"] == distance[smallest] and state[ghost_row][ghost_col + 1] in (77, 71, 66, 11, 10):
                return "R"
            elif distance["D"] == distance[smallest] and state[ghost_row + 1][ghost_col] in (77, 71, 66, 11, 10):
                return "D"
            elif distance["L"] == distance[smallest] and state[ghost_row][ghost_col - 1] in (77, 71, 66, 11, 10):
                return "L"
            elif distance["U"] == distance[smallest] and state[ghost_row - 1][ghost_col] in (77, 71, 66, 11, 10):
                return "U"
            distance[smallest] = float("inf")
            smallest = min(distance.items(), key=lambda x: x[1])[0]

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        ghosts = {50: [None, None], 40: [None, None], 30: [None, None], 20: [None, None]}
        packman_row, packman_col = self.find_row_col(state, 66)
        for i in ghosts.keys():
            ghosts[i][0], ghosts[i][1] = self.find_row_col(state, i)
            if ghosts[i][0] == None and ghosts[i][1] == None:
                ghosts[i][0], ghosts[i][1] = self.find_row_col(state, i+1)

        state = [list(i) for i in state]
        row_mov = 0
        col_mov = 0
        if action == "R":
            col_mov = 1
        elif action == "L":
            col_mov = (-1)
        elif action == "U":
            row_mov = (-1)
        else:
            row_mov = 1

        if state[packman_row + row_mov][packman_col + col_mov] == 11 or 10:
             state[packman_row][packman_col] = 10
             state[packman_row + row_mov][packman_col + col_mov] = 66
        elif state[packman_row + row_mov][packman_col + col_mov] == 99:
            pass
        else:
            state[packman_row][packman_col] = 10
            state[packman_row + row_mov][packman_col + col_mov] = 88
        packman_row = packman_row + row_mov
        packman_col = packman_col + col_mov


        ghost_action = ""
        ghost_order = [50, 20, 30, 40]
        for i in ghost_order:
            if ghosts[i][0] == None:
                continue
            ghost_row = ghosts[i][0]
            ghost_col = ghosts[i][1]
            ghost_action = self.manhattan_distance(state, ghost_row, ghost_col, packman_row, packman_col)
            row_mov = 0
            col_mov = 0
            if ghost_action == "R":
                col_mov = 1
            elif ghost_action == "L":
                col_mov = (-1)
            elif ghost_action == "U":
                row_mov = (-1)
            else:
                row_mov = 1

            if state[ghost_row + row_mov][ghost_col + col_mov] == 66:
                state[ghost_row][ghost_col] = 10
                state[ghost_row + row_mov][ghost_col + col_mov] = 88
                break
            elif state[ghost_row + row_mov][ghost_col + col_mov] == 10:
                if i in state[ghost_row]:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + row_mov][ghost_col + col_mov] = i
                else:
                    state[ghost_row][ghost_col] = 11
                    state[ghost_row + row_mov][ghost_col + col_mov] = i
            elif state[ghost_row + row_mov][ghost_col + col_mov] == 11:
                if i in state[ghost_row]:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + row_mov][ghost_col + col_mov] = i+1
                else:
                    state[ghost_row][ghost_col] = 11
                    state[ghost_row + row_mov][ghost_col + col_mov] = i+1
            elif state[ghost_row + row_mov][ghost_col + col_mov] == 77:
                if i in state[ghost_row]:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + row_mov][ghost_col + col_mov] = 10
                else:
                    state[ghost_row][ghost_col] = 11
                    state[ghost_row + row_mov][ghost_col + col_mov] = 10
            elif state[ghost_row + row_mov][ghost_col + col_mov] == 71:
                if i in state[ghost_row]:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + row_mov][ghost_col + col_mov] = 11
                else:
                    state[ghost_row][ghost_col] = 11
                    state[ghost_row + row_mov][ghost_col + col_mov] = 11
        return tuple(tuple(i) for i in state)


    def goal_test(self, state):
        """ Given a state, checks if this is the goal state, compares to the created goal state"""
        for row in state:
            if 11 in row or 21 in row or 31 in row or 41 in row or 51 in row or 71 in row:
                return False
        return True


    def distance_toxic_ghost(self, state):
        toxic = []
        dist = 0
        for row in state:
            for col in row:
                if col == 71:
                    toxic.append((state.index(row),row.index(col)))
        min_dist_per_tox = float('inf')
        min_dist = 0
        ghost_counter=0
        if not toxic:
            return 0
        for i in range(len(toxic)):
            for row in state:
                for col in row:
                    if col == 51 or col == 50 or col == 41 or col == 40 or col == 31 or col == 30 or col == 21 or col == 20:
                        ghost_counter+=1
                        dist = abs(state.index(row) - toxic[i][0])+abs(row.index(col)-toxic[i][1])
                        if dist<min_dist_per_tox:
                            min_dist_per_tox=dist
            if min_dist_per_tox>min_dist:
                min_dist=min_dist_per_tox
        if ghost_counter<len(toxic):
            return float('Inf')
        return min_dist

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""
        pacman_row, packman_col = self.find_row_col(node.state, 66)
        if pacman_row == None:
            return float('inf')
        elif node.state[pacman_row + 1][packman_col] in (51, 50, 40, 41, 30, 31, 20, 21) or node.state[pacman_row - 1][packman_col] in (51, 50, 40, 41, 30, 31, 20, 21) or node.state[pacman_row][packman_col + 1] in (51, 50, 40, 41, 30, 31, 20, 21) or node.state[pacman_row][packman_col - 1] in (51, 50, 40, 41, 30, 31, 20, 21):
            return float('inf')
        else:
            points_left = self.point_sum(node.state)
            closest_dot_dist = 0
            dist_tox_ghost = 0
            closest_dot_dist, farest_dot_dist = closest_dot_distance(node.state, pacman_row,packman_col)
            dist_tox_ghost = self.distance_toxic_ghost(node.state)
            if (points_left + closest_dot_dist)<dist_tox_ghost:
                return dist_tox_ghost
            if (points_left + closest_dot_dist)<farest_dot_dist:
                return farest_dot_dist
            return (points_left + closest_dot_dist)



    """Feel free to add your own functions"""


def create_pacman_problem(game):
    return PacmanProblem(game)

