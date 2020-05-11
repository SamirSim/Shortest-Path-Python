from djikstra import *
from graph import graphs as graphInit
from copy import copy, deepcopy

graphs = deepcopy(graphInit)

costs = [(1,10), (1000,1), (10,1000)]
#costs = [(1,1), (1,1), (1,1)]

for (weight_migration, weight_overload) in costs:

  i = 0
  print("Migration Weight:", weight_migration, "Overload Weight:", weight_overload, " : ")
  for (edges, vertices) in graphs:
    currentEdges = []; currentVertices = []
    currentEdges = deepcopy(edges)
    currentVertices = deepcopy(vertices)
    nbVertices = len(edges)
    #start = input('Start cell  : (From 0 to ' + str(nbVertices-1) + '): ')
    #target = input('End cell  : (From 0 to ' + str(nbVertices-1) + '): ')
    start = 0
    target = 67
    previous = []
    previous, probabilities = djikstra(currentVertices, currentEdges, start, weight_migration, weight_overload)
    path, distance, nbMigrations, nbOverloadedCells = shortest(currentEdges, previous, start, target, weight_migration, weight_overload, probabilities)
    print("Graph:", i , "Path:", path, "Distance:",  distance, "Nb Migrations:", nbMigrations, "Nb Overloaded cells:", nbOverloadedCells)
    i = i + 1
#print(probabilities)

    

"""
nbVertices = len(edges_6)
start = input('Start cell  : (From 0 to ' + str(nbVertices-1) + '): ')
target = input('End cell  : (From 0 to ' + str(nbVertices-1) + '): ')
start = int(start)
target = int(target)
previous = []
previous = djikstra(vertices_6, edges_6, start)
print(shortest(edges_6, previous, start, target))
"""
