from Blocker import Blocker
import copy
from PathsAlgo import find_all_paths

class OmnicientBlocker(Blocker):
    def __init__(self): 
        return

    def play(self, position, graph, goal):
        move=self.blockerPlay(position,graph,goal, 5, -1000, 1000)
        print('removed'+str(move[1]))
        graph[move[1][0]][move[1][1]]-=1
        return

    # Does a minmax algorithm. -1000=runner wins, 1000=blocker wins
    # return value = (win/lose,edge to remove)
    def blockerPlay(self, position, graph, goal, level, alpha, beta):
        retEdge=(-1,-1)
        for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0:
                    graph[a][c]-=1
                    score=self.runnerPlay(position,graph,goal,level,alpha,beta)
                    graph[a][c]+=1
                    if score>alpha:
                        alpha=score
                        retEdge=(a,c)
                        if alpha>=beta:
                            return(alpha,retEdge)
        return (alpha,retEdge)

    def runnerPlay(self, position,graph, goal, level, alpha, beta):
        for (a,b) in enumerate(graph[position]):
            if b>0:
                if a==goal:
                    return -1000
                else:
                    if level==0:
                        score=-1000+len(find_all_paths(graph, a, goal))
                    else:
                        score=self.blockerPlay(a,graph,goal,level-1,alpha,beta)[0]
                    if score<beta:
                        beta=score
                        if alpha>=beta:
                            return beta
        return min
