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
from Blocker import Blocker
from RandomBlocker import RandomBlocker


class Graphe:
    def __init__(self):
        return;
    

class Runner:
    def __init__(self): 
        return;
    def play(self,position,graphe,goal):
        res = -1;
        return res;
            
        
if __name__ == '__main__':
    
    print ('debut main');
    
    runner = Runner();
    blocker = Blocker();
    graphe = Graphe();
    goal = 1;
        
    run = True;
    
    ###
    while(run):
        runnerRes = runner.play(0,graphe,1);
        if(runnerRes == -1 or runnerRes == goal):
            run=False;
            if(runnerRes==goal):
                print('runner win');
            else:
                print('runner lose');
                
        blocker.play(0, graphe);            
    ###
    
    print ('fin du programme');
    
