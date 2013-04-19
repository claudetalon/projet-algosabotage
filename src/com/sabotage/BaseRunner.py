from PathsAlgo import find_all_paths
from PathsAlgo import vertex_of_optimized_path
from Runner import Runner

class BaseRunner(Runner):

    def __init__(self, graph, current, goal):
        self._graph = graph
        self._current = current
        self._goal = goal
        
    '''
	We don't need time, that's the default Runner
    '''
    def play(self, current, graph, goal, time):
        pathsList = find_all_paths(graph, current, goal)
        return vertex_of_optimized_path(graph, pathsList)
