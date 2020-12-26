import numpy as np
import time
from agent import Agent
from othello import Othello, Node


def writeToFile(size, white_depth, black_depth, avg_white_time, avg_black_time, total_game_time, white_score,
                black_score, avg_branch_white, eff_branch_white, avg_branch_black, eff_branch_black):
    f = open("Result.txt", "a")
    f.write("Board size: " + str(size) + "\n")
    f.write("White depth: " + str(white_depth) + "\n")
    f.write("Black depth: " + str(black_depth) + "\n")
    f.write("Average white turn time: " + str(avg_white_time) + " sec\n")
    f.write("Average black turn time: " + str(avg_black_time) + " sec\n")
    f.write("Total game time: " + str(total_game_time) + " sec\n")
    f.write("White score:" + str(white_score) + "\n")
    f.write("Black score:" + str(black_score) + "\n")
    f.write("Average branching factor (White agent): " + str(avg_branch_white) + "\n")
    f.write("Effective branching factor (White agent): " + str(eff_branch_white) + "\n")
    f.write("Average branching factor (Black agent): " + str(avg_branch_black) + "\n")
    f.write("Average branching factor (Black agent): " + str(eff_branch_black) + "\n")
    f.write("=======================================================================================\n")
    f.close()


if __name__ == "__main__":
    n = 8  # Size of othello board
    white_depth = 1  # Depth of white agent tree
    black_depth = 8  # Depth of black agent tree
    game_over = 0  # Equals 2 when both black and white can't play
    num_turns_white = 0  # Number of turns of white agent
    num_turns_black = 0  # Number of turns of black agent
    white_playing_time = 0      # White time playing
    black_playing_time = 0      # Black time playing
    othello = Othello(n)
    white = Agent(1, othello.heuristic, othello.normalMoveGenerator)
    black = Agent(-1, othello.heuristic, othello.normalMoveGenerator)
    print("Initial State")
    print(othello.state)
    # Game loop
    start = time.time()
    while (not othello.checkGameState()) and game_over < 2:
        state_node = Node(n)
        # White turn
        state_node.state = np.copy(othello.state)
        start_white_time = time.time()
        value, state = white.alphaBetaPruning(state_node, white_depth, -10e15, 10e15, True, white.turn)
        white_playing_time += (time.time() - start_white_time)
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
        start_black_time = time.time()
        value, state = black.alphaBetaPruning(state_node, black_depth, -10e15, 10e15, False, black.turn)
        black_playing_time += (time.time() - start_black_time)
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
    total_time = end - start
    print("======================== Game Over !!! ===========================")
    white_score = np.count_nonzero(othello.state == 1)
    black_score = np.count_nonzero(othello.state == -1)
    print("White score:", white_score)
    print("Black score:", black_score)
    print("============================ Time ================================")
    print("Time elapsed = ", total_time, " sec")
    print("==================== Average branching factor ====================")
    avg_branch_white = (white.traversed_nodes / (white.traversed_nodes - white.leaf_nodes))
    eff_branch_white = (np.power(white.traversed_nodes / (white_depth * num_turns_white), 1 / white_depth))
    print("Average branching factor (White agent) = ", avg_branch_white)
    print("Effective branching factor (White agent) = ", eff_branch_white)
    avg_branch_black = (black.traversed_nodes / (black.traversed_nodes - black.leaf_nodes))
    eff_branch_black = (np.power(black.traversed_nodes / (black_depth * num_turns_black), 1 / black_depth))
    print("Average branching factor (Black agent) = ", avg_branch_black)
    print("Effective branching factor (Black agent) = ", eff_branch_black)
    writeToFile(n, white_depth, black_depth, white_playing_time/num_turns_white, black_playing_time/num_turns_black,
                total_time, white_score, black_score, avg_branch_white, eff_branch_white,
                avg_branch_black, eff_branch_black)
