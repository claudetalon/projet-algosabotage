from Blocker import Blocker
from random import randint
from Trace import writeIntoFile

class RandomBlocker(Blocker):
    def __init__(self): 
        return

    def play(self, position, graph, goal):
    
        nbEdges=0
        for i in graph:
            for j in i:
                nbEdges+=j
                
        removed=randint(0,nbEdges-1)
        for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0:
                    if removed<d:
                        graph[a][c]-=1
                        writeIntoFile('removed '+'('+str(a)+','+str(c)+')')
                        return
                    else:
                        removed-=d
        return
