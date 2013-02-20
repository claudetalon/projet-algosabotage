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
from Runner import Runner
        
if __name__ == '__main__':
    
    print ('debut main')
    
    run = True
    
    '''
    goal = 1
    current = 2    
    graph = [[0,1,0,1],[0,0,1,0],[1,0,0,1],[0,1,0,0]]
    '''
     
    goal = 2
    current = 0   
    graph =[[0,1,0],[0,0,1],[1,0,0]]
    
    runner = Runner(graph, current, goal)
    blocker = RandomBlocker()
   
   
    print ('runner start '+str(runner.current)+' goal '+str(runner.goal))
    ###
    while(run):
        newPos = runner.play(graph, current, goal);        
        print ('runner old position '+str(current)+' new position '+str(newPos))
        
        current=newPos;
        if(current == -1 or current == goal):
            run=False;
            if(current==goal):
                print('runner win');
            else:
                print('runner lose');
            continue
        
        blocker.play(0, graph);            
    ###
    
    print ('fin du programme');
    
