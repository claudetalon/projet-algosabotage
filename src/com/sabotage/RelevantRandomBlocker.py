from Blocker import Blocker
from random import randint
from Trace import writeIntoFile
from PathsAlgo import getInterestingGraph

class RelevantRandomBlocker(Blocker):

    """
    Random blocker
    This blocker removes one edge randomly with equal probabilities
    """

    def __init__(self): 
        return

    def play(self, position, graph, goal, time):
    
        # Compute the number of edges
        igraph=getInterestingGraph(position,graph,goal)
        nbEdges=0
        for i in igraph:
            for j in i:
                nbEdges+=j
        
        # Remove one edge randomly
        removed=randint(0,nbEdges-1)
        for (a,b) in enumerate(igraph):
            for (c,d) in enumerate(b):
                if d>0:
                    if removed<d:
                        graph[a][c]-=1
                        writeIntoFile('removed '+'('+str(a)+','+str(c)+')')
                        return
                    else:
                        removed-=d
        return
