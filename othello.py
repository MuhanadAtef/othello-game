import numpy as np


class Node:
    def __init__(self, n):
        self.value = None
        self.child = []
        self.state = np.zeros((n, n))


class Othello:
    def __init__(self, size, turn):
        self.size = size  # Size of othello board
        self.game_over = False  # To check if the game is over
        initial_node = np.zeros((self.size, self.size))
        initial_node[n // 2 - 1][n // 2 - 1] = -1
        initial_node[n // 2][n // 2] = -1
        initial_node[n // 2 - 1][n // 2] = 1
        initial_node[n // 2][n // 2 - 1] = 1
        self.state = initial_node  # Hold the state node of othello board
        self.turn = turn  # 1 for white, -1 for black

    # Here we will check for each disc and check for disc (left, right, diagonal)
    # to see if we can place discs to flip the opponent discs
    # This function returns all possible movements and their results to the board state
    def whereToPlaceDiscs(self, state, discs):
        states_dictionary = {}
        for i in range(len(discs[0])):
            disc = [discs[0][i], discs[1][i]]
            # ==========================================================================================
            # ========================== Check where to place the new Disc =============================
            # ==========================================================================================

            # --------------------------------- Left -------------------------------------
            # Check if there is an disc with different color on the left of current disc
            left_disc = np.copy(disc)
            left_disc[1] -= 1
            add_disc = True
            if disc[1] > 0 and state[left_disc[0]][left_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[left_disc[0]][left_disc[1]] != 0 and left_disc[1] >= 0:
                    if state[left_disc[0]][left_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    left_disc[1] -= 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and left_disc[1] >= 0:
                    key = tuple(left_disc)
                    if key in states_dictionary.keys():
                        states_dictionary[key][disc[0], left_disc[1]:disc[1] + 1] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        state_tmp[disc[0], left_disc[1]:disc[1] + 1] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Right -------------------------------------
            # Check if there is an disc with different color on the right of current disc
            right_disc = np.copy(disc)
            right_disc[1] += 1
            add_disc = True
            if disc[1] < self.size - 1 and state[right_disc[0]][right_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[right_disc[0]][right_disc[1]] != 0 and right_disc[1] <= self.size - 1:
                    if state[right_disc[0]][right_disc[1]] == state[disc[0]][
                        disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    right_disc[1] += 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and right_disc[1] <= self.size - 1:
                    key = tuple(right_disc)
                    if key in states_dictionary.keys():
                        states_dictionary[key][disc[0], disc[1]:right_disc[1] + 1] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        state_tmp[disc[0], disc[1]:right_disc[1] + 1] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Up -------------------------------------
            # Check if there is an disc with different color on the up of current disc
            up_disc = np.copy(disc)
            up_disc[0] -= 1
            add_disc = True
            if disc[0] > 0 and state[up_disc[0]][up_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[up_disc[0]][up_disc[1]] != 0 and up_disc[0] >= 0:
                    if state[up_disc[0]][up_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    up_disc[0] -= 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and up_disc[0] >= 0:
                    key = tuple(up_disc)
                    if key in states_dictionary.keys():
                        states_dictionary[key][up_disc[0]:disc[0] + 1, disc[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        state_tmp[up_disc[0]:disc[0] + 1, disc[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Down -------------------------------------
            # Check if there is an disc with different color on the bottom of current disc
            down_disc = np.copy(disc)
            down_disc[0] += 1
            add_disc = True
            if disc[0] < self.size - 1 and state[down_disc[0]][down_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[down_disc[0]][down_disc[1]] != 0 and down_disc[0] <= self.size - 1:
                    if state[down_disc[0]][down_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    down_disc[0] += 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and down_disc[1] <= self.size - 1:
                    key = tuple(down_disc)
                    if key in states_dictionary.keys():
                        states_dictionary[key][disc[0]:down_disc[0] + 1, disc[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        state_tmp[disc[0]:down_disc[0] + 1, disc[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Up Left -------------------------------------
            # Check if there is an disc with different color on the up-left of current disc
            up_left_disc = np.copy(disc)
            up_left_disc[1] -= 1
            up_left_disc[0] -= 1
            add_disc = True
            if disc[1] > 0 and disc[0] > 0 and state[up_left_disc[0]][up_left_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[up_left_disc[0]][up_left_disc[1]] != 0 and (up_left_disc[1] >= 0 and up_left_disc[0] >= 0):
                    if state[up_left_disc[0]][up_left_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    up_left_disc[1] -= 1
                    up_left_disc[0] -= 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and (up_left_disc[1] >= 0 and up_left_disc[0] >= 0):
                    key = tuple(up_left_disc)
                    list1 = range(up_left_disc[0], disc[0] + 1)
                    list2 = range(up_left_disc[1], disc[1] + 1)
                    indices = [[list1[i], list2[i]] for i in range(len(list1))]
                    if key in states_dictionary.keys():
                        for index in indices:
                            states_dictionary[key][index[0]][index[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        for index in indices:
                            state_tmp[index[0]][index[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Up Right -------------------------------------
            # Check if there is an disc with different color on the up-right of current disc
            up_right_disc = np.copy(disc)
            up_right_disc[1] += 1
            up_right_disc[0] -= 1
            add_disc = True
            if disc[1] < self.size - 1 and disc[0] > 0 and state[up_right_disc[0]][up_right_disc[1]] == -state[disc[0]][
                disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[up_right_disc[0]][up_right_disc[1]] != 0 and (
                        up_right_disc[1] <= self.size - 1 and up_right_disc[0] >= 0):
                    if state[up_right_disc[0]][up_right_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    up_right_disc[1] += 1
                    up_right_disc[0] -= 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and (up_right_disc[1] <= self.size - 1 and up_right_disc[0] >= 0):
                    key = tuple(up_right_disc)
                    list1 = range(disc[0], up_right_disc[0] + 1)
                    list2 = range(up_right_disc[1], disc[1] + 1)
                    indices = [[list1[i], list2[i]] for i in range(len(list1))]
                    if key in states_dictionary.keys():
                        for index in indices:
                            states_dictionary[key][index[0]][index[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        for index in indices:
                            state_tmp[index[0]][index[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Down Left -------------------------------------
            # Check if there is an disc with different color on the down-left of current disc
            down_left_disc = np.copy(disc)
            down_left_disc[1] -= 1
            down_left_disc[0] += 1
            add_disc = True
            if disc[1] > 0 and disc[0] < self.size - 1 and state[down_left_disc[0]][down_left_disc[1]] == - \
                    state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[down_left_disc[0]][down_left_disc[1]] != 0 and (
                        down_left_disc[1] >= 0 and down_left_disc[0] <= self.size - 1):
                    if state[down_left_disc[0]][down_left_disc[1]] == state[disc[0]][disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    down_left_disc[1] -= 1
                    down_left_disc[0] += 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and (down_left_disc[1] >= 0 and down_left_disc[0] <= self.size - 1):
                    key = tuple(down_left_disc)
                    list1 = range(disc[0], down_left_disc[0] + 1)
                    list2 = range(down_left_disc[1], disc[1] + 1)
                    indices = [[list1[i], list2[i]] for i in range(len(list1))]
                    if key in states_dictionary.keys():
                        for index in indices:
                            states_dictionary[key][index[0]][index[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        for index in indices:
                            state_tmp[index[0]][index[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp

            # --------------------------------- Down Right -------------------------------------
            # Check if there is an disc with different color on the down-right of current disc
            down_right_disc = np.copy(disc)
            down_right_disc[1] += 1
            down_right_disc[0] += 1
            add_disc = True
            if disc[1] < self.size - 1 and disc[0] < self.size - 1 and state[down_right_disc[0]][
                down_right_disc[1]] == -state[disc[0]][disc[1]]:
                # Loop until find a gap or disc of the same color
                while state[down_right_disc[0]][down_right_disc[1]] != 0 and (
                        down_right_disc[1] <= self.size - 1 and down_right_disc[0] <= self.size - 1):
                    if state[down_right_disc[0]][down_right_disc[1]] == state[disc[0]][
                        disc[1]]:  # Disc of the same color
                        add_disc = False
                        break
                    down_right_disc[1] += 1
                    down_right_disc[0] += 1
                # Add disc if it will cause a change in state (discs flip)
                if add_disc and (down_right_disc[1] <= self.size - 1 and down_right_disc[0] <= self.size - 1):
                    key = tuple(down_right_disc)
                    list1 = range(disc[0], down_right_disc[0] + 1)
                    list2 = range(disc[1], down_right_disc[1] + 1)
                    indices = [[list1[i], list2[i]] for i in range(len(list1))]
                    if key in states_dictionary.keys():
                        for index in indices:
                            states_dictionary[key][index[0]][index[1]] = state[disc[0]][disc[1]]
                    else:
                        state_tmp = np.copy(state)
                        for index in indices:
                            state_tmp[index[0]][index[1]] = state[disc[0]][disc[1]]
                        states_dictionary[key] = state_tmp
        children = list(states_dictionary.values())
        return children

    # state -> the current state to get its children
    # depth -> depth of the tree
    # turn -> white if turn ==1 and black if -1
    def normalMoveGenerator(self, state_node, depth, turn):
        if depth == 0:
            state_node.value = self.evaluate(state_node.state)
            return
        # Get indices of white/black discs of the state
        ones = np.where(state_node.state == turn)
        children = self.whereToPlaceDiscs(state_node.state, ones)
        for child in children:
            node = Node(self.size)
            node.state = child
            state_node.child.append(node)
            self.normalMoveGenerator(node, depth - 1, turn * -1)

    # state -> state to be evaluated
    def evaluate(self, state):
        return np.sum(state)


if __name__ == "__main__":
    n = 8
    othello = Othello(n, 1)
    state = othello.state
    state_node = Node(othello.size)
    state_node.state = state
    othello.normalMoveGenerator(state_node, 3, othello.turn)
    othello.turn *= -1
    print(state)
