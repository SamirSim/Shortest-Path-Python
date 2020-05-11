import sys
from random import seed
import random 

MIGRATION_COST = 10

def init_graph(dist, graphG, start):
	for s in range(len(graphG)):
		dist[s] = sys.maxsize
	dist[start] = 0

def find_min(dist, q):
	minD = sys.maxsize
	vertex = -1
	for s in q:
		if dist[s] < minD:
			minD = dist[s]
			vertex = s
	return vertex

def update_dist(dist, previous, edges, s1, s2, weight_migration, weight_overload):
	"""
	if dist[s2] > dist[s1] + weight_migration * edges[s1][s2] + edges[s2][s2]:
		dist[s2] = dist[s1] + weight_migration * edges[s1][s2] + weight_overload * edges[s2][s2]
		previous[s2] = s1
	"""
	if dist[s2] > dist[s1] + edges[s1][s2] + edges[s2][s2]:
		dist[s2] = dist[s1] + edges[s1][s2] + edges[s2][s2]
		previous[s2] = s1
	
	return dist, previous

def djikstra(vertices, edges, start, weight_migration, weight_overload):
	dist, previous, nbVertices, nodes, edges, probabilities = init(edges, weight_migration, weight_overload)
	init_graph(dist, nodes, start)
	q = nodes
	while len(q) > 0:
		s1 = find_min(dist, q)
		q.remove(s1)
		for s2 in range(nbVertices):
			if vertices[s1][s2] == 1:
				dist, previous = update_dist(dist, previous, edges, s1, s2, weight_migration, weight_overload)
	return previous, probabilities

def shortest(edges, previous, start, target, weight_migration, weight_overload, probabilities):
	path = []
	nbMigrations, nbOverloadedCells, distance = 0, 0, 0
	s = target
	while s != start:
		path.append(s)
		#print(edges[s][s] / WEIGHT_OVERLOAD)
		distance = distance + edges[s][previous[s]] + edges[s][s]
		if edges[s][previous[s]] == weight_migration * MIGRATION_COST: 
			nbMigrations = nbMigrations + 1
		s = previous[s]
	path.append(start)
	path.reverse()
	for i in path:
		#print(probabilities[i])
		if probabilities[i] > 0.5:
			nbOverloadedCells = nbOverloadedCells + 1
	return path, distance, nbMigrations, nbOverloadedCells

def init(edges, weight_migration, weight_overload):
	dist = []
	previous = []
	nodes = []
	nbVertices = len(edges)
	for i in range(nbVertices):
		nodes.append(i)
		dist.append(sys.maxsize)
		previous.append(0)

	# seed random number generator
	seed(1)
	probabilities = []
	
	# generate random numbers between 0-1
	for _ in range(nbVertices):
		probabilities.append(random.uniform(0,1))
	for i in range(nbVertices):
		edges[i][i] = weight_overload * probabilities[i]
		#edges[i][i] = probabilities[i]
		for j in range(nbVertices):
			if edges[i][j] == MIGRATION_COST:
				edges[i][j] = weight_migration * MIGRATION_COST

	return dist, previous, nbVertices, nodes, edges, probabilities
