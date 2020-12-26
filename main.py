import numpy as np
import time
from agent import Agent
from othello import Othello, Node

if __name__ == "__main__":
    n = 8      # Size of othello board
    white_depth = 5     # Depth of white agent tree
    black_depth = 5     # Depth of black agent tree
    game_over = 0   # Equals 2 when both black and white can't play
    num_turns_white = 0     # Number of turns of white agent
    num_turns_black = 0     # Number of turns of black agent
    othello = Othello(n)
    white = Agent(1, othello.heuristic, othello.orderedMoveGenerator)
    black = Agent(-1, othello.heuristic, othello.normalMoveGenerator)
    # Game loop
    start = time.time()
    while (not othello.checkGameState()) and game_over < 2:
        state_node = Node(n)
        # White turn
        state_node.state = np.copy(othello.state)
        value, state = white.alphaBetaPruning(state_node, white_depth, -10e15, 10e15, True, white.turn)
        # If white can play then change the game state
        if state is not None:
            num_turns_white += 1
            game_over = 0
            othello.state = state
            print("White turn")
            print(othello.state, "\n")
        else:
            game_over += 1
        if othello.checkGameState():
            break
        # Black turn
        state_node = Node(n)
        state_node.state = np.copy(othello.state)
        value, state = black.alphaBetaPruning(state_node, black_depth, -10e15, 10e15, False, black.turn)
        # If black can play then change the game state
        if state is not None:
            num_turns_black += 1
            game_over = 0
            othello.state = state
            print("Black turn")
            print(othello.state, "\n")
        else:
            game_over += 1
    end = time.time()
    print("======================== Game Over !!! ===========================")
    print("White score:", np.count_nonzero(othello.state == 1))
    print("Black score:", np.count_nonzero(othello.state == -1))
    print("============================ Time ================================")
    print("Time elapsed = ", str(end - start), " sec")
    print("==================== Average branching factor ====================")
    print("Average branching factor (White agent) = ", np.ceil(white.traversed_nodes / (white.traversed_nodes - white.leaf_nodes)))
    print("Effective branching factor (White agent) = ", np.ceil(np.power(white.num_branches/(white_depth * num_turns_white), 1 / white_depth)))
    print("Average branching factor (Black agent) = ", np.ceil(black.traversed_nodes / (black.traversed_nodes - black.leaf_nodes)))
    print("Effective branching factor (Black agent) = ", np.ceil(np.power(black.num_branches/(black_depth * num_turns_black), 1 / white_depth)))
