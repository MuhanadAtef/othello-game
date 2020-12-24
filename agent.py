class Agent:
    # game -> game object
    # turn -> 1 for white and -1 for black
    def __init__(self, game, turn):
        self.game = game
        self.turn = turn

    # root -> current state of the tree
    # depth -> depth of the tree
    # alpha -> alpha value
    # beta -> beta value
    def alphaBetaPruning(self, root, depth, alpha, beta, maximize):
        # If we reach leaves of the tree then select generator to goto next state
        if not root.child or depth == 0:
            # Check if the evaluation value is computed
            if root.value == None:
                root.value = self.game.evaluate(root.state)
            return root.value, None
        optimal_move = root.state
        if maximize:
            max_evaluation = -10e15
            for i in root.child:
                evaluation, _ = self.alphaBetaPruning(i, depth - 1, alpha, beta, not maximize)
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
                evaluation, _ = self.alphaBetaPruning(i, depth - 1, alpha, beta, not maximize)
                # Update min value and beta
                if min_evaluation > evaluation:
                    optimal_move = i.state
                    min_evaluation = evaluation
                beta = min(beta, min_evaluation)
                if beta <= alpha:
                    break
            root.value = min_evaluation
            return min_evaluation, optimal_move
