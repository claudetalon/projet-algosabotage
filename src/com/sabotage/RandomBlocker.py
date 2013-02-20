from Blocker import Blocker
from random import randint

class RandomBlocker(Blocker):
    def __init__(self): 
        return

    def play(self, position, graph):
    
        nbEdges=0
        for i in graph:
            for j in i:
                nbEdges+=j
                
        removed=randint(0,nbEdges-1)
        print ('removed '+str(removed))
        for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0:
                    if removed<d:
                        graph[a][c]-=1
                        return
                    else:
                        removed-=d
        return
