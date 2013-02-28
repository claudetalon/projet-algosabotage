from random import randint

def matrixRandomGenerator(vertex, edges):

    matrix = []
    for i in range(0, vertex) :
        line = []
        for j in range(0, vertex) :
            line = line + [0]

        matrix = matrix + [line]

    for i in range(0, edges) :
        matrix[randint(0,vertex-1)][randint(0,vertex-1)] += 1

    return matrix
