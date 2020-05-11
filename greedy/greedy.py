import sys
from random import seed
import random 

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

def primMST(graphTop, mst, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD): 
	graphTop, probabilities = init(graphTop, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD) 
	V = len(graphTop)
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
				if graphTop[i][j] + graphTop[j][j]< minn: 
					if isValidEdge(i, j, inMST): 
						minn = graphTop[i][j] + graphTop[j][j]
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

def bfs(graphTop, start, end):
		queue = []
		visited = []
		queue.append([start])
		while queue:
				path = queue.pop(0)
				node = path[-1]
				visited.append(node)
				if node == end:
						return path
				for adjacent in graphTop.get(node, []):
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

def init(graphTop, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD):
	#print(MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD)

	nbVertices = len(graphTop)
	# seed random number generator
	probabilities = []
	seed(1)

	# generate random numbers between 0-1
	for _ in range(nbVertices):
		probabilities.append(random.uniform(0,1))

	for i in range(nbVertices):
		graphTop[i][i] = WEIGHT_OVERLOAD * probabilities[i]

	for i in range(nbVertices):
		for j in range(nbVertices):
			#print(i,j,graph[i][j])
			if graphTop[i][j] == MIGRATION_COST:
								#print(i, j, WEIGHT_MIGRATION * MIGRATION_COST)
				graphTop[i][j] = WEIGHT_MIGRATION * MIGRATION_COST

				#print(WEIGHT_MIGRATION, MIGRATION_COST, graph[i][j])
	
	return graphTop, probabilities

def shortest(path, graphTop, target, MIGRATION_COST, WEIGHT_MIGRATION, WEIGHT_OVERLOAD, probabilities):
	nbMigrations, nbOverloadedCells, distance = 0, 0, 0

	for i in range(len(path)-1):
		current = path[i]
		next = path[i+1]
		distance = distance + graphTop[current][next] + graphTop[next][next]
		#print(current, next, graph[current][next], WEIGHT_MIGRATION * MIGRATION_COST)
		if graphTop[current][next] == WEIGHT_MIGRATION * MIGRATION_COST: 
			nbMigrations = nbMigrations + 1

	for i in path:
		#print(probabilities[i])
		if probabilities[i] > 0.5:
			nbOverloadedCells = nbOverloadedCells + 1

	return distance, nbMigrations, nbOverloadedCells
