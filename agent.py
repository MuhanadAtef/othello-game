class Agent:
    # turn -> 1 for white and -1 for black
    # heuristic -> game evaluation function
    # move_generator -> generating moves function
    def __init__(self, turn, heuristic, move_generator):
        self.turn = turn
        self.heuristic = heuristic
        self.move_generator = move_generator

    # root -> current state of the tree
    # depth -> depth of the tree
    # alpha -> alpha value
    # beta -> beta value
    def alphaBetaPruning(self, root, depth, alpha, beta, maximize, turn):
        self.move_generator(root, depth, turn, self.heuristic, self.turn)
        # If we reach leaves of the tree then select generator to goto next state
        if not root.child or depth == 0:
            # Check if the evaluation value is computed
            if root.value is None:
                root.value = self.heuristic(root.state, self.turn)
            return root.value, None
        optimal_move = root.state
        if maximize:
            max_evaluation = -10e15
            for i in root.child:
                evaluation, _ = self.alphaBetaPruning(i, depth - 1, alpha, beta, not maximize, -turn)
                # Update max value and alpha
                if max_evaluation < evaluation:
                    optimal_move = i.state
                    max_evaluation = evaluation
                alpha = max(alpha, max_evaluation)
                if beta <= alpha:
                    break
            root.value = max_evaluation
            return max_evaluation, optimal_move
        else:
            min_evaluation = 10e15
            for i in root.child:
                evaluation, _ = self.alphaBetaPruning(i, depth - 1, alpha, beta, not maximize, -turn)
                # Update min value and beta
                if min_evaluation > evaluation:
                    optimal_move = i.state
                    min_evaluation = evaluation
                beta = min(beta, min_evaluation)
                if beta <= alpha:
                    break
            root.value = min_evaluation
            return min_evaluation, optimal_move
