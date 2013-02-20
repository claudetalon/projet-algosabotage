from Blocker import Blocker
from random import randint

class RandomBlocker(Blocker):
    def __init__(self): 
        return

    def play(self, position, graph):
        nbEdges=0
        for a in graph:
            for b in a:
                nbEdges+=b
        removed=radint(0,nbEdges-1)
        for (a,b) in graph:
            for (c,d) in b:
                if d>0:
                    if removed<d:
                        graph[a][c]-=1
                        return
                    else:
                        removed-=d
        return
