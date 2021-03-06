# coding=UTF-8

from RandomBlocker import RandomBlocker
from OmnicientBlocker import OmnicientBlocker
from FinishBlocker import FinishBlocker
from BaseRunner import BaseRunner
from Runner_Alpha_Beta import Runner_Alpha_Beta
from Trace import writeIntoFile
from Matrix import maxtrixListGenerator

if __name__ == '__main__':
    
    
    
    '''
    goal = 1
    current = 2    
    graph = [[0,1,0,1],[0,0,1,0],[1,0,0,1],[0,1,0,0]]
    '''
    
    ''' 
    goal = 2
    current = 0   
    graph =[[0,1,0],[0,0,1],[1,0,0]]
    '''
    '''
    graph = [[0,1,0,0,1,0,0,0,0],
             [1,0,2,1,1,0,0,0,0],
             [0,0,0,1,0,0,1,0,0],
             [0,0,0,0,0,2,0,0,0],
             [1,0,0,0,0,1,0,0,0],
             [0,0,0,0,0,0,0,2,0],
             [0,0,0,0,0,2,0,0,1],
             [0,0,0,0,0,0,1,0,2],
             [0,0,0,0,0,0,0,0,0]]
    '''
        
    ''' graphs types '''
    nbVertex = 10
    nbEdges = 51

    ''' graph list length '''
    nbGraph = 10

    graphList = maxtrixListGenerator(nbGraph, nbVertex, nbEdges)

    for i in range(0, nbGraph-1) :
        run = True
        graph = graphList[i]
        current = 0
        goal = nbVertex -1

        writeIntoFile('begin')

        runner = BaseRunner(graph, current, goal)
        blocker = OmnicientBlocker()
        #blocker = FinishBlocker()
        blocker.setupBlocker(current,graph,goal)
   
        writeIntoFile('runner start '+str(runner._current)+' goal '+str(runner._goal))
        ###
        while(run):
            newPos = runner.play(current, graph, goal, 5)
            writeIntoFile('runner old position '+str(current)+' new position '+str(newPos))
            current=newPos
            if(current == -1 or current == goal):
                run=False
                if(current==goal):
                    writeIntoFile('runner has won')
                else:
                    writeIntoFile('runner has lost')
                continue
            blocker.play(current, graph, goal, 5)
        ###
        writeIntoFile('end')
