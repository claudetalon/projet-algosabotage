from random import randint

def find_all_paths(graph, start, end, path=[]):

    if start == end and path == []:
        return []

    path = path + [start]
    if start == end:
        return [path]
    
    if start > len(graph):
        return []
    
    paths = []
    
    # Calcul des successeurs de start
    l = []
    for i,j in enumerate(graph[start]):
        if graph[start][i] >= 1:
            l.append(i)
    
    for node in l:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)
                
    return paths

def vertex_of_optimized_path(graph, pathsList):
    
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
            edgesEquality.clear()
            edgesEquality.append(l[edges[i]])
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

if __name__ == '__main__':
    graph = [[0,2,0,1],[0,0,1,0],[1,0,0,1],[0,1,0,0]]
    print(vertex_of_optimized_path(graph, find_all_paths(graph, 2, 0,[])))
