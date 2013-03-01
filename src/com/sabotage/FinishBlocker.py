from OmnicientBlocker import OmnicientBlocker
from PathsAlgo import find_all_paths
from PathsAlgo import edges_number
from Trace import writeIntoFile

class FinishBlocker(OmnicientBlocker):

    def __init__(self):
        print ('init finish blocker')
        super().__init__();        
        self.startBlockingAtGoal=False;
        return


    '''
    on recherche le plus court chemin possible
    à faire une seule fois avant de commencer le jeu
    pour évaluer si oui ou non ca vaut la peine d'enlever toutes les aretes du goal
    '''
    def setupBlocker(self,begin,graph,goal):
        
        '''chercher tout les chemins entre le debut et l arrivee'''
        pathlist = find_all_paths(graph, begin, goal)
        
        '''chercher le plus court chemin possible'''
        minpathlist = sorted(pathlist, key = lambda p : len(p) )
        
        minpath=minpathlist[0]
        
        '''regarder si il y a plusieurs meilleurs chemins de taille egale'''
        equalminpath=[]
        for path in pathlist :
            if len(path) == len(minpath) :
                equalminpath.append(path)

        '''cherche le chemin ayant le plus d'aretes parmis les chemins minimum'''
        if(len(equalminpath)>1): 
            strp=''  
            for p in equalminpath :
                strp+=str(p)+' '+ str(edges_number(p,graph))+' '
            print('equalminpath '+str(len(equalminpath))+ ' : '+strp)
            
            minpath = max(equalminpath, key=lambda p: edges_number(p,graph))
            
                        
        lengthminpath = len(minpath)
        nbedgesminpath = edges_number(minpath,graph)
        
        print('setup blocker ' + str(len(pathlist))+ ' path min path is ' + str(minpath) + ' with length '+ str(lengthminpath) 
              + ' with ' +str(nbedgesminpath)+' edges')
        
        numberOfRunnerTurn=len(minpath)-1
        
        '''nombre d'aretes relié au noeud goal'''
        goalEdges=0
        for index , node in enumerate(graph):
            if(index!=goal):
                goalEdges+=node[goal]
        
        print('runner min turn '+str(numberOfRunnerTurn)+' goalEdges '+str(goalEdges))

        '''commencer a enlever les aretes a partir de la fin si numberOfRunnerTurn > goalEdges'''
        
        if(numberOfRunnerTurn>goalEdges) : 
            print('use goal blocking')
            self.startBlockingAtGoal=True
        else :
            print('don\'t use goal blocking')            
            self.startBlockingAtGoal=False
        
        
    def play(self, position, graph, goal):
        
        if(self.startBlockingAtGoal) :
            self.blockGoal(graph,goal)            
        else :
            super().play(position,graph,goal)
        return
    
    def blockGoal(self,graph,goal):
        removed=-1
        for index , node in enumerate(graph):
            if(index!=goal):
                if(node[goal]>0):
                    removed=index
                    node[goal]-=1
                    break
                
        print ('removed edge of node '+str(removed))
        return
        
        
        
        