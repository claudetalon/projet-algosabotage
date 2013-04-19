from Blocker import Blocker
import copy
from PathsAlgo import find_all_paths
from Trace import writeIntoFile
from threading import Thread
from time import clock
from Runner import Runner

class Runner_Alpha_Beta(Runner):

    def __init__(self, graph, current, goal):
        self._graph = graph
        self._current = current
        self._goal = goal
        self.maxLevel=1
        self.bestScore=-10000
        
    def getInterestingGraph(self,position,graph,goal):
          size=len(graph)
          iGraph=[[0]*size for _ in range(size)]
          for path in find_all_paths(graph, position, goal):
              maxEdge=len(path)-1
              for a in range(0,maxEdge):
                src=path[a]
                dst=path[a+1]
                iGraph[src][dst]=graph[src][dst]
          return iGraph
        
    def blockerPlay(self, position, graph, goal, level, alpha, beta):
          if self.timeout:
            return(-10000,(0,0))
          retEdge=(-1,-1)
          for (a,b) in enumerate(graph):
            for (c,d) in enumerate(b):
                if d>0 and d<=level+1:
                    graph[a][c]-=1
                    score=self.runnerPlay(position,graph,goal,level,alpha,beta,(a,c),d-1)[0]
                    graph[a][c]+=1
                    if score>alpha:
                        alpha=score
                        retEdge=(a,c)
                        if alpha>=beta:
                            return(alpha,retEdge)
          return (alpha,retEdge)    
        
    # RunnerPlay
    # lastRemove -> dernier arc enlevé
    # nEges -> poids restant de l'arc
    def runnerPlay(self, position,graph, goal, level, alpha, beta, lastRemove, nEdges):
          meilleurCoup = -1
          if self.timeout:
            return (-1,-1)
          for (a,b) in enumerate(graph[position]):
            if b>0:
                if a==goal:
                    return (-10000, a) # Runner wins
                else:
                    if level==0:
                        score=10000-len(find_all_paths(graph, a, goal, [position,a])) # A la fin de l'arbre
                    else:
                        if nEdges>0:
                            start=lastRemove[0]
                            stop=lastRemove[1]
                            graph[start][stop]-=1
                            score=self.runnerPlay(a,graph,goal,level-1,alpha,beta, lastRemove, nEdges-1)[0]
                            graph[start][stop]+=1
                        else:
                            score=self.blockerPlay(a,graph,goal,level-1,alpha,beta)[0]
                    if score<beta:
                        meilleurCoup = a
                        beta=score
                        if alpha>=beta:
                            return (beta, a)
          return (beta, meilleurCoup)

    # runnerThread
    def runnerThread(self,position,graph,goal):
       newMove=self.runnerPlay(position,graph,goal, self.maxLevel,-10000, 10000, (-1,-1), 0)
       if not self.timeout:
         self.move=newMove
          
    def play(self, position, graph, goal, time):
        startTime=clock()

        self.timeout=False

        # Search only on pertinent edges
        interestingGraph=self.getInterestingGraph(position, graph, goal)

        # At least, always try with a level 1 search
        self.move=self.runnerPlay(position,interestingGraph,goal, 0, -10000, 10000, (-1,-1), 0)

        # Loop for trying differents depths
        if clock()-startTime<time:
            while self.move[0]!=-10000 and self.maxLevel<10 and not self.timeout:
                self.maxLevel+=1
                thread = Thread(target = self.runnerThread, args=(position,interestingGraph,goal))
                thread.start()
                thread.join(startTime-clock()+time)
                if thread.isAlive():
                    self.timeout=True
                    self.maxLevel-=1
                    writeIntoFile('timeout')
        if self.move[0]==-10000:
            self.maxLevel-=2
        else:
            self.maxLevel-=1

        # If not move is found, remove the first edge
        if(self.move[1]==(-1,-1)):
            for (a,b) in enumerate(interestingGraph):
                        for (c,d) in enumerate(b):
                            if d>0:
                                self.move=(-10000,(a,c))
        if self.move[0]>self.bestScore:
            self.bestScore=self.move[0]
        return self.move[1]