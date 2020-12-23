# root -> current state of the tree
# depth -> depth of the tree
# alpha -> alpha value
# beta -> beta value
# maximize -> choose the current state to maximize (True), or minimize (False)
def alphaBetaPruning(root, depth, alpha, beta, maximize):
    # If we reach leaves of the tree then select generator to goto next state
    if not root.child or depth == 0:
        return root.value
    if maximize:
        max_evaluation = -10e15
        for i in root.child:
            evaluation = alphaBetaPruning(i, depth - 1, alpha, beta, not maximize)
            # Update max value and alpha
            max_evaluation = max(max_evaluation, evaluation)
            alpha = max(alpha, max_evaluation)
            if beta <= alpha:
                break
        root.value = max_evaluation
        return max_evaluation
    else:
        min_evaluation = 10e15
        for i in root.child:
            evaluation = alphaBetaPruning(i, depth - 1, alpha, beta, not maximize)
            # Update min value and beta
            min_evaluation = min(min_evaluation, evaluation)
            beta = min(alpha, min_evaluation)
            if beta <= alpha:
                break
        root.value = min_evaluation
        return min_evaluation

