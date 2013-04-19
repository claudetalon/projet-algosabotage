class Runner:
    """Abstract blocker class"""

    def __init__(self): 
        return

    """
    Play a move. Removes one edge from the graph.
    Parameters:
        position : runner's position
        graph : current graph
        goal : goal node
        time : time limit to compute the move
    Return value : none
    """
    def play(self, position, graph, goal, time):
        pass
		
