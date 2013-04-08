from Blocker import Blocker
from random import randint
from Trace import writeIntoFile

class RandomBlocker(Blocker):

    """
    Random blocker
    This blocker removes one edge randomly with equal probabilities
    """

    def __init__(self): 
        return

    def play(self, position, graph, goal, time):
        self.randomRemove(position, graph, graph, goal, time)

    def randomRemove(self, position, removeGraph, searchGraph, time):
        # Compute the number of edges
        nbEdges=0
        for i in searchGraph:
            for j in i:
                nbEdges+=j
        
        # Remove one edge randomly
        removed=randint(0,nbEdges-1)
        for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0:
                    if removed<d:
                        removeGraph[a][c]-=1
                        writeIntoFile('removed '+'('+str(a)+','+str(c)+')')
                        return
                    else:
                        removed-=d
        return
