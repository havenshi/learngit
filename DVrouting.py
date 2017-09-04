import numpy as np
import collections
import os
from numpy import genfromtxt
import pandas as pd
import json
import itertools

class Graph:
    def __init__(self):
        # initial values of V, E and W as empty list or dict
        self.nodes = [] # keep single node
        self.vertices = []
        self.edges = {}
        self.weights = {}
        self.paths = {} # record each path

    def add_vertex(self, value):
        if value not in self.vertices:
            self.vertices.append(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        # from and to vertices are different, and there's path between them
        if from_vertex in self.edges:  # add edges of one node into map
            if to_vertex not in self.edges[from_vertex]:
                self.edges[from_vertex].append(to_vertex)
        else:
            self.edges[from_vertex] = [to_vertex]
        if to_vertex in self.edges:  # flooding the table to neighbors
            if from_vertex not in self.edges[to_vertex]:
                self.edges[to_vertex].append(from_vertex)
        else:
            self.edges[to_vertex] = [from_vertex]

        # use DV to update distance to each neighbor
        if (from_vertex, to_vertex) not in self.weights:  # add each path
            self.weights[(from_vertex, to_vertex)] = distance
            self.paths[(from_vertex, to_vertex)] = [to_vertex]

        if (to_vertex, from_vertex) not in self.weights:
            self.weights[(to_vertex, from_vertex)] = distance
            self.paths[(to_vertex, from_vertex)] = [from_vertex]


    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights) + "\n"
        return string


def dv(center, nodes, vertices, edges, weights, paths):
    visited = [] # traversal all node, forward table to its neighbor
    queue = [center] # record the neighbor of node
    while queue: # use stack or BFS
        center = queue.pop(0)
        for node in edges[center]: # send table to its neighbor nodes
            if node not in visited:
                for dest in [x for x in nodes if x != node]: # each neighbor nodes has a table to all possible destination
                    if (node, dest) not in weights and (center, dest) not in weights:  # if not find dest is in node table
                        weights[(node, dest)] = float('-inf')
                        weights[(dest, node)] = float('-inf')
                        paths[(node, dest)] = []
                        paths[(dest, node)] = []
                    # if find dest is in center table
                    elif (center, dest) in weights and ((node, dest) not in weights or ((node, dest) in weights and weights[(node, dest)] > weights[(node, center)] + weights[(center, dest)])):
                        #  Dx(y) <- minv{c(x,v) + Dv(y)}
                        weights[(node, dest)] = weights[(node, center)] + weights[(center, dest)]
                        weights[(dest, node)] = weights[(node, center)] + weights[(center, dest)]
                        paths[(node, dest)] = [center] + paths[(center, dest)]
                        paths[(dest, node)] = paths[(dest, center)] + [node]

                queue.append(node) # add each node(neighbor of center) and next step is to visit all neighbors

        visited.append(center)


# main function
print "==================================================="
print "\nCS6543 Distance Vector Routing Simulator\n"
print "1.Read Existing Network Topology File"
print "2.Add a New Node"
print "3.Calculate Shortest Path to Destination Router"
print "4.Exit"
print "\n==================================================="

# select command
command = 0
G = Graph()  # initial graph
matrix = [[None]]

# Run program till exit.
while command != 4:
    command = input("\nCommand: ")

    if command == 1:  # upload file
        f = open('data3.txt', 'r')  # read data from file and write into matrix
        matrix = json.loads(f.read())

        n = len(matrix)
        for i in range(1, n):
            G.nodes.append(str(matrix[i][0]))
            G.add_vertex(str(matrix[i][0]))
            for j in range(1, n):
                if matrix[i][j] != 0 and matrix[i][j] != -1:
                    G.add_edge(str(matrix[i][0]), str(matrix[j][0]), matrix[i][j])

            dv(str(matrix[i][0]), G.nodes, G.vertices, G.edges, G.weights, G.paths)

        print 'The current network is:'
        print G

    elif command == 2:  # create network by inputting port numbers and cost and write into matrix
        n = len(matrix)

        port = input('node ')
        G.nodes.append(port) # nodes only add once
        G.add_vertex(port)

        if port in matrix[0]:
            pass
        else:
            # add one row
            matrix.append([-1] * (n + 1))
            matrix[n][0] = port
            matrix[n][n] = 0

            # add one column
            for i in range(n):
                if i == 0:
                    matrix[i].append(port)
                else:
                    matrix[i].append(-1)

        while True:
            neighbor, cost = input('Enter neighbors (neighbor and cost with a comma in between): ')
            if neighbor == -1 and cost == -1:  # exit input, jump out of the loop
                break
            else:
                G.add_vertex(neighbor)
                G.add_edge(port, neighbor, cost)

                if neighbor in matrix[0]:
                    row = matrix[0].index(port)
                    column = matrix[0].index(neighbor)
                    matrix[row][column] = cost
                    matrix[column][row] = cost
                else:
                    n = len(matrix)
                    # add one row
                    matrix.append([-1] * (n + 1))
                    matrix[n][0] = neighbor
                    matrix[n][n] = 0

                    # add one column
                    for i in range(n):
                        if i == 0:
                            matrix[i].append(neighbor)
                        else:
                            matrix[i].append(-1)

                    row = matrix[0].index(port)
                    matrix[row][n] = cost
                    matrix[n][row] = cost

        # set the new node as center node, traversal tables of other nodes, update distance
        dv(port, G.nodes, G.vertices, G.edges, G.weights, G.paths)

        print 'The LSA from node %s is:' % (port)
        print G  # after a new node added to the network, print the current view of the network at the node

    elif command == 3:
        # store shortest cost from node to node and its path into a routing table

        n = len(matrix) - 1
        table = [[-1] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                if i == j:
                    table[i][j] = 0  # the cost from node to itself is 0
                else:
                    start = G.vertices[i]
                    end = G.vertices[j]
                    distance = float('inf')
                    if (start, end) in G.weights:
                        distance = G.weights[(start, end)]
                    pathlist = ''
                    if (start, end) in G.weights:
                        pathlist = start + '->' + '->'.join(str(x) for x in G.paths[(start, end)])
                    table[i][j] = [distance, pathlist]

        print 'The shortest path tree is:'
        for i in range(n):
            print table[i]
        print '\n'

        # generate routing table
        for i in range(n):
            print 'Routing table at node %s' % (G.vertices[i])
            print 'Destination' + '\t' + 'Next Node' + '\t' + 'Cost'
            for j in range(n):
                if j != i:  # extract path and cost from each node
                    paths = table[i][j][1].split('->')  # next node is the second node from the start node
                    print str(G.vertices[j]) + '\t' + paths[1] + '\t' + str(table[i][j][0])

# Exit if command is 4.
print "\nExit CS6543 project. Thanks!\n"

