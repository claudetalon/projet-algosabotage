from Blocker import Blocker
import copy
from PathsAlgo import find_all_paths
from Trace import writeIntoFile
from threading import Thread

class OmnicientBlocker(Blocker):
    def __init__(self):
        self.maxLevel=1
        return

    def play(self, position, graph, goal, time):
        self.timeout=False
        self.move=self.blockerPlay(position,graph,goal, 1, -10000, 10000) 
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
        if(self.move[1]==(-1,-1)):
            for (a,b) in enumerate(graph):
                        for (c,d) in enumerate(b):
                            if d>0:
                                self.move[1]=(a,c)
        writeIntoFile('removed'+str(self.move[1]))
        graph[self.move[1][0]][self.move[1][1]]-=1
        return


    def blockerThread(self,position,graph,goal):
        newMove=self.blockerPlay(position,graph,goal, self.maxLevel, -10000, 10000)
        if not self.timeout:
            self.move=newMove

    # Does a minmax algorithm. -10000=runner wins, 10000=blocker wins
    # return value = (win/lose,edge to remove)
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
