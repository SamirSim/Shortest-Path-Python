import sys
from random import seed
import random 

seed(3)

from sys import maxsize 
INT_MAX = maxsize 
V = 68


def isValidEdge(u, v, inMST): 
	if u == v: 
		return False
	if inMST[u] == False and inMST[v] == False: 
		return False
	elif inMST[u] == True and inMST[v] == True: 
		return False
	return True

def primMST(graph, mst, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD): 
	graph, probabilities = init(graph, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD) 
	V = len(graph)
	mst = [[0 for i in range(V)] for j in range(V)]
	inMST = [False] * V 

	inMST[0] = True

	edge_count = 0
	mincost = 0
	while edge_count < V - 1: 

		minn = INT_MAX 
		a = -1
		b = -1
		for i in range(V): 
			for j in range(V): 
				if graph[i][j] + graph[j][j]< minn: 
					if isValidEdge(i, j, inMST): 
						minn = graph[i][j] + graph[j][j]
						a = i 
						b = j 

		if a != -1 and b != -1: 
			#print("Edge %d: (%d, %d) cost: %f" %
				#(edge_count, a, b, minn)) 
			mst[a][b] = b
			mst[b][a] = a
			edge_count += 1
			mincost += minn 
			inMST[b] = inMST[a] = True

	#print("Minimum cost =", mincost) 
	
	return mst, probabilities

def bfs(graph, start, end):
		queue = []
		visited = []
		queue.append([start])
		while queue:
				path = queue.pop(0)
				node = path[-1]
				visited.append(node)
				if node == end:
						return path
				for adjacent in graph.get(node, []):
					if adjacent not in visited:
						new_path = list(path)
						new_path.append(adjacent)
						queue.append(new_path)

def genGraphDict(mst):
	graphDict = {}
	for node in range(len(mst)):
		adjacents = []
		for adjacent in mst[node]:
			if adjacent != 0:
				adjacents.append(adjacent)
		graphDict[node] = adjacents
	return graphDict

def init(graph, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD):
	nbVertices = len(graph)
	# seed random number generator
	probabilities = []
	# generate random numbers between 0-1
	for _ in range(nbVertices):
		probabilities.append(random.uniform(0,1))

	for i in range(nbVertices):
		graph[i][i] = WEIGHT_OVERLOAD * probabilities[i]
		for j in range(nbVertices):
			if graph[i][j] == MIGRATION_COST:
				graph[i][j] = WEIGHT_MIGRATION * graph[i][j]
	
	return graph, probabilities

def shortest(path, graph, target, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD, probabilities):
	nbMigrations, nbOverloadedCells, distance = 0, 0, 0

	for i in range(len(path)-1):
		current = path[i]
		next = path[i+1]
		distance = distance + graph[current][next] + graph[next][next]

		if graph[current][next] == WEIGHT_MIGRATION * MIGRATION_COST: 
			nbMigrations = nbMigrations + 1

	for i in path:
		#print(probabilities[i])
		if probabilities[i] > 0.5:
			nbOverloadedCells = nbOverloadedCells + 1

	return distance, nbMigrations, nbOverloadedCells