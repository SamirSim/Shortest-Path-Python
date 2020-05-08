from djikstra import *
from graph import graphs

MIGRATION_COST = 10

costs = [(1,10), (10,10), (10,100)]

for (weight_migration, weight_overload) in costs:
  i = 0
  print("Migration Weight:", weight_migration, "Overload Weight:", weight_overload, " : ")
  for (edges, vertices) in graphs:
    nbVertices = len(edges)
    #start = input('Start cell  : (From 0 to ' + str(nbVertices-1) + '): ')
    #target = input('End cell  : (From 0 to ' + str(nbVertices-1) + '): ')
    start = 0
    target = 67
    previous = []
    previous, probabilities = djikstra(vertices, edges, start, MIGRATION_COST, weight_migration, weight_overload)
    path, distance, nbMigrations, nbOverloadedCells = shortest(edges, previous, start, target, MIGRATION_COST, weight_migration, weight_overload, probabilities)
    print("Graph:", i , "Path:", path, "Distance:",  distance, "Nb Migrations:", nbMigrations, "Nb Overloaded cells:", nbOverloadedCells)
    i = i + 1
    

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