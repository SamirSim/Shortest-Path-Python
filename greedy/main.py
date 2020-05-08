from greedy import *
from graph import graphs
from random import seed
import random 

seed(3)
MIGRATION_COST = 10

costs = [(1,10), (10,10), (10,100)]

for (weight_migration, weight_overload) in costs:
	i = 0
	print("Migration Weight:", weight_migration, "Overload Weight:", weight_overload, " : ")
	for (edges, vertices) in graphs:
		graph = edges
		#start = input('Start cell  : (From 0 to ' + str(nbVertices-1) + '): ')
		#target = input('End cell  : (From 0 to ' + str(nbVertices-1) + '): ')
		start = 0
		target = 67
		mst = [[]]
		mst, probabilities = primMST(graph, mst, MIGRATION_COST, weight_migration, weight_overload)
		graphDict = genGraphDict(mst)
		path = bfs(graphDict, start, target)
		distance, nbMigrations, nbOverloadedCells = shortest(path, graph, target, MIGRATION_COST, weight_migration, weight_overload, probabilities)
		print("Graph:", i , "Path:", path, "Distance:",  distance, "Nb Migrations:", nbMigrations, "Nb Overloaded cells:", nbOverloadedCells)
		i = i + 1
