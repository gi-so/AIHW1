import search
import random
import math


ids = ["111111111", "111111111"]


class PacmanProblem(search.Problem):
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

    def find_row_col(self, state, agent):
        row = None
        col = None
        for row in state:
            if agent in row:
                row = state.index(row)
                col = row.index(agent)
        return row, col

    def manhattan_distance(self, state, ghost_row, ghost_col, packman_row, packman_col):

    def result(self, state, action):
        """Return the state that results from executing the given
        action in the given state. The action must be one of
        self.actions(state)."""
        ghosts = {50: [None, None], 40: [None, None], 30: [None, None], 20: [None, None]}
        packman_row, packman_col = self.find_row_col(self, state, 66)
        for i in ghosts.keys():
            ghosts[i][0], ghosts[i][1] = self.find_row_col(self.state, i)
            if ghosts[i][0] == None and ghosts[i][1] == None:
                ghosts[i][0], ghosts[i][1] = self.find_row_col(self.state, i+1)

        state = list(state)
        if action == "R":
            if state[packman_row][packman_col + 1] == 11 or 10:
                state[packman_row][packman_col] = 10
                state[packman_row][packman_col + 1] = 66
                packman_col = packman_col + 1
            elif state[packman_row][packman_col + 1] == 99:
                pass
            else:
                state[packman_row][packman_col] = 10
                state[packman_row][packman_col + 1] = 88
                packman_col = packman_col + 1
        elif action == "L":
            if state[packman_row][packman_col - 1] == 11 or 10:
                state[packman_row][packman_col] = 10
                state[packman_row][packman_col - 1] = 66
                packman_col = packman_col - 1
            elif state[packman_row][packman_col - 1] == 99:
                pass
            else:
                state[packman_row][packman_col] = 10
                state[packman_row][packman_col - 1] = 88
                packman_col = packman_col - 1
        elif action == "U":
            if state[packman_row - 1][packman_col] == 11 or 10:
                state[packman_row][packman_col] = 10
                state[packman_row - 1][packman_col] = 66
                packman_row = packman_row - 1
            elif state[packman_row - 1][packman_col] == 99:
                pass
            else:
                state[packman_row][packman_col] = 10
                state[packman_row - 1][packman_col] = 88
                packman_row = packman_row - 1
        elif action == "D":
            if state[packman_row + 1][packman_col] == 11 or 10:
                state[packman_row][packman_col] = 10
                state[packman_row + 1][packman_col] = 66
                packman_row = packman_row + 1
            elif state[packman_row + 1][packman_col] == 99:
                pass
            else:
                state[packman_row][packman_col] = 10
                state[packman_row + 1][packman_col] = 88
                packman_row = packman_row + 1
        ghost_action = ""
        ghost_order = [50, 20, 30, 40]
        for i in ghost_order:
            if ghosts[i][0] == None:
                continue
            ghost_row = ghosts[i][0]
            ghost_col = ghosts[i][1]
            ghost_action = self.manhattan_distance(self, state, ghost_row, ghost_col, packman_row, packman_col)

            if ghost_action == "R":
                if state[ghost_row][ghost_col + 1] == 11 or 10:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row][ghost_col + 1] = 66
                elif state[ghost_row][ghost_col + 1] == 99:
                    pass
                else:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row][ghost_col + 1] = 88
            elif ghost_action == "L":
                if state[ghost_row][ghost_col - 1] == 11 or 10:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row][ghost_col - 1] = 66
                elif state[ghost_row][ghost_col - 1] == 99:
                    pass
                else:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row][ghost_col - 1] = 88
            elif ghost_action == "U":
                if state[ghost_row - 1][ghost_col] == 11 or 10:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row - 1][ghost_col] = 66
                elif state[ghost_row - 1][ghost_col] == 99:
                    pass
                else:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row - 1][ghost_col] = 88
            elif ghost_row == "D":
                if state[ghost_row + 1][ghost_col] == 11 or 10:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + 1][ghost_col] = 66
                elif state[ghost_row + 1][ghost_col] == 99:
                    pass
                else:
                    state[ghost_row][ghost_col] = 10
                    state[ghost_row + 1][ghost_col] = 88

        return state


    def goal_test(self, state):
        """ Given a state, checks if this is the goal state, compares to the created goal state"""
        for row in state:
            if 11 in row or 21 in row or 31 in row or 41 in row or 51 in row or 71 in row:
                return False
        return True

    def h(self, node):
        """ This is the heuristic. It gets a node (not a state,
        state can be accessed via node.state)
        and returns a goal distance estimate"""

    """Feel free to add your own functions"""


def create_pacman_problem(game):
    return PacmanProblem(game)

