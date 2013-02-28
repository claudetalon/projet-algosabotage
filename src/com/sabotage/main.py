# coding=UTF-8
'''
Created on 19 févr. 2013

@author: kim
'''

'''
class OmnicientBlocker:
def play(position, graph)

class RandomBlocker:
def play(position, graph)
-> graphe modifié

class Runner:
def play(graph, currentPosition, goal)
-> return sommet ou -1 si perdu
'''
from RandomBlocker import RandomBlocker
from OmnicientBlocker import OmnicientBlocker
from Runner import Runner
from Trace import writeIntoFile
from Matrix import matrixRandomGenerator
import os

if __name__ == '__main__':
    
    print ('debut main')
    
    run = True
    
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
    nbVertex = 10
    nbEdges = 25
    graph = matrixRandomGenerator(nbVertex, nbEdges)
    writeIntoFile(str(graph))
    current = 0
    goal = nbVertex - 1

    runner = Runner(graph, current, goal)
    blocker = OmnicientBlocker()
   
    writeIntoFile('begin')

    writeIntoFile('runner start '+str(runner.current)+' goal '+str(runner.goal))
    ###
    while(run):
        newPos = runner.play(graph, current, goal)
        
        if (newPos != -1):
            writeIntoFile('runner old position '+str(current)+' new position '+str(newPos))
        
        current=newPos
        if(current == -1 or current == goal):
            run=False
            if(current==goal):
                writeIntoFile('runner has won')
            else:
                writeIntoFile('runner has lost')
            continue

        blocker.play(current, graph, goal)            
    ###

    writeIntoFile('end')
