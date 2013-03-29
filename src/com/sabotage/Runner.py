from PathsAlgo import find_all_paths
from PathsAlgo import vertex_of_optimized_path

class Runner(object):

    def __init__(self, graph, current, goal):
        self._graph = graph
        self._current = current
        self._goal = goal
        
    def play(self, graph, current, goal):
        pathsList = find_all_paths(graph, current, goal)
        return vertex_of_optimized_path(graph, pathsList)
    @property
    def graph(self):
        return self._graph
    
    @property
    def current(self):
        return self._current
    
    @property
    def goal(self):
        return self._goal
    
    @graph.setter
    def graph(self, graph):
        self._graph = graph
        
    @current.setter
    def current(self, current):
        self._current = current
        
    @goal.setter
    def goal(self, goal):
        self._goal = goal