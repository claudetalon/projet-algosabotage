from PathsAlgo import find_all_paths

class Runner(object):

    def __init__(self, graph, current, goal):
        self._graph = graph
        self._current = current
        self._goal = goal
        self.maxLevel=1
        self.bestScore=-10000
        
        def blockerPlay(self, position, graph, goal, level, alpha, beta):
	    if self.timeout:
	      return(-10000,(0,0))
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
        
        # TODO : Method
        def play(self, level, alpha, beta):
	  for (a,b) in enumerate(graph[current]):
            if b>0:
                if a==goal:
                    return a
                else:
                    if level==0:
                        score=10000-len(find_all_paths(graph, a, goal))
                    else:
                        score=self.blockerPlay(a,graph,goal,level-1,alpha,beta)[0]
                    if score<beta:
                        beta=score
                        if alpha>=beta:
                            return beta
        return beta