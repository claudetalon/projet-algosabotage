from Blocker import Blocker
import copy

class OmnicientBlocker(Blocker):
    def __init__(self): 
        return

    def play(self, position, graph, goal):
        move=self.blockerPlay(position,graph,goal)
        print('removed'+str(move[1]))
        graph[move[1][0]][move[1][1]]-=1
        return

    # Does a minmax algorithm. -1=runner wins, 1=blocker wins
    # return value = (win/lose,edge to remove)
    def blockerPlay(self, position, graph, goal):
        score=1
        retEdge=(-1,-1)
        for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0:
                    newGraph=copy.deepcopy(graph)
                    newGraph[a][c]-=1
                    score=self.runnerPlay(position,newGraph,goal)
                    if score==1:
                        return (1,(a,c))
                    retEdge=(a,c)
        return (score,retEdge)

    def runnerPlay(self, position,graph, goal):
        score=1
        for (a,b) in enumerate(graph[position]):
            if b>0:
                if a==goal:
                    return -1
                else:
                    score=self.blockerPlay(a,graph,goal)[0]
                    if score==-1:
                        return -1
        return score
