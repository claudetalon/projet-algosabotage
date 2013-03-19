from random import randint
from Trace import writeIntoFile

def findSuccessors(graph):
    successors=[]
    for a,b in enumerate(graph):
        nodeSuccessors=[]
        for c,d in enumerate(b):
            if d>=1:
                nodeSuccessors.append(c)
        successors.append(nodeSuccessors)
    return successors

def find_all_paths(graph, start, end, path=[], ignored=[], successors=[]):

    if (start == end and path == []) or start > len(graph):
        return []

    path = path + [start]

    if ignored == [] :
        ignored = [0]*len(graph)

    if successors == []:
        successors = findSuccessors(graph)

    if start == end:
        return [path]

    ignored[start] += 1    
    paths = []
    
    l = successors[start]

    for node in l:
        if ignored[node] == 0:
            newpaths = find_all_paths(graph, node, end, path, ignored, successors)
            paths.extend(newpaths)

    ignored[start] -= 1   
    return paths

def vertex_of_optimized_path(graph, pathsList):

    valpath = str(len(pathsList))
    writeIntoFile('The runner has found paths : ' + valpath)
    #writeIntoFile(str(pathsList))

    # Cannot go to goal
    if len(pathsList) == 0:
        return -1
    
    minimum = len(pathsList[0])
    for path in pathsList[1:]:
        minimum = min(len(path), minimum)
    
    l = []
    
    for path in pathsList:
        if len(path) == minimum:
            l.append(path)
          
    if len(l) == 1:
        # Vertex to go
        return l[0][1]
    
    # Calculating the best way (several paths)
    edges = []
    for path in l:
        edges.append(edges_number(path, graph))
        
    maxEdges = edges[0]
    edgesEquality = [l[0]] # If same edges number
    
    i = 0
    
    for i in range(1, len(edges)):
        if edges[i] > maxEdges:
            maxEdges = edges[i]
            edgesEquality = []
            edgesEquality.append(l[i])
        elif edges[i] == maxEdges:
            edgesEquality.append(l[i])
        
    if len(edgesEquality) == 1:
        return l[i][1]
        
    # Several edges number equalities
    return l[randint(0,len(edgesEquality)-1)][1]
        
def edges_number(path, graph):
    edges = 0
    for i in range(0, len(path)-1):
        edges = edges + graph[path[i]][path[i+1]]

    return edges
