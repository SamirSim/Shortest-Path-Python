from greedy import *
from graph import graphs
from graph import graphs as graphInit
from copy import copy, deepcopy

graphs = deepcopy(graphInit)

MIGRATION_COST = 10

costs = [(1,10), (10000,1), (10,10000)]

for (weight_migration, weight_overload) in costs:
	i = 0
	print("Migration Weight:", weight_migration, "Overload Weight:", weight_overload, " : ")
	for edges in graphs:
		#graphTop = edges
		#start = input('Start cell  : (From 0 to ' + str(nbVertices-1) + '): ')
		#target = input('End cell  : (From 0 to ' + str(nbVertices-1) + '): ')
		currentEdges = deepcopy(edges)
		start = 0
		target = 67
		mst = [[]]
		mst, probabilities = primMST(currentEdges, mst, MIGRATION_COST, weight_migration, weight_overload)
		graphDict = genGraphDict(mst)
		path = bfs(graphDict, start, target)
		distance, nbMigrations, nbOverloadedCells = shortest(path, currentEdges, target, MIGRATION_COST, weight_migration, weight_overload, probabilities)
		print("Graph:", i , "Path:", path, "Distance:",  distance, "Nb Migrations:", nbMigrations, "Nb Overloaded cells:", nbOverloadedCells)
		i = i + 1
