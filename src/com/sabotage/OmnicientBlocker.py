from Blocker import Blocker
import copy
from PathsAlgo import find_all_paths
from Trace import writeIntoFile
from threading import Thread

class OmnicientBlocker(Blocker):

    """
    Omnicient blocker
    This blocker tries to remove the right edges to prevent the runner from
    reaching the goal.
    """
    def __init__(self):
        self.maxLevel=1
        return

    """
    Main function
    Spaws a threas which does an alpha-beta algorithm.
    It tries with a low depth, and if there is not a winning strategy, 
    it tries with deeper searches, until the time is out ot it has found
    a winning strategy.
    """
    def play(self, position, graph, goal, time):
        self.timeout=False
        self.move=self.blockerPlay(position,graph,goal, 1, -10000, 10000)

        # Loop for trying differents depths
        while self.move[0]!=10000 and self.maxLevel<5 and not self.timeout:
            self.maxLevel+=1
            thread = Thread(target = self.blockerThread, args=(position,graph,goal))
            thread.start()
            thread.join(time)
            if thread.isAlive():
                self.timeout=True
                self.maxLevel-=1
                writeIntoFile('timeout')
        if self.move[0]==10000:
            self.maxLevel-=2
        else:
            self.maxLevel-=1

        # If not move is found, remove the first edge
        if(self.move[1]==(-1,-1)):
            for (a,b) in enumerate(graph):
                        for (c,d) in enumerate(b):
                            if d>0:
                                self.move[1]=(a,c)
        writeIntoFile('removed'+str(self.move[1]))
        graph[self.move[1][0]][self.move[1][1]]-=1
        return

    """
    blockerThread
    The main function of the alpha-beta thread.
    Calls the alpha-beta function, and keeps the result only if it has
    found a move in time.
    """
    def blockerThread(self,position,graph,goal):
        newMove=self.blockerPlay(position,graph,goal, self.maxLevel, -10000, 10000)
        if not self.timeout:
            self.move=newMove

    """
    blockerPlay
    Does an alpha-beta algorithm go get the best move.
    This method plays the blocker. This is the MAX nodes.
    Parameters:
        position: runner's position
        graph: current graph
        goal: runner's goal
        level: depth of the search
        alpha: current alpha value
        beta: current beta value
    Return value = (score,edge to remove)
    -10000=runner wins, 10000=blocker wins
    """
    def blockerPlay(self, position, graph, goal, level, alpha, beta):
        if self.timeout:
            return(0,(0,0))
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

    """
    runnerPlay
    Does an alpha-beta algorithm go get the best move.
    This method plays the runner. This is the MIN nodes.
    Parameters:
        position: runner's position
        graph: current graph
        goal: runner's goal
        level: depth of the search
        alpha: current alpha value
        beta: current beta value
    Return value = score
    -10000=runner wins, 10000=blocker wins
    If neither player wins or looses, the score is based on the number of paths
    to the goal.
    """

    def runnerPlay(self, position,graph, goal, level, alpha, beta):
        if self.timeout:
            return 0
        for (a,b) in enumerate(graph[position]):
            if b>0:
                if a==goal:
                    return -10000
                else:
                    if level==0:
                        score=-10000+len(find_all_paths(graph, a, goal))
                    else:
                        score=self.blockerPlay(a,graph,goal,level-1,alpha,beta)[0]
                    if score<beta:
                        beta=score
                        if alpha>=beta:
                            return beta
        return beta
