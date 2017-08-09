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
    for node in [_ for _ in nodes if _ != center]: # find nodes aside from center, node = '2222'
        # add indirect path
        if (center, node) not in weights:
            for neighbor in edges[center]:
                if (node, neighbor) in weights:
                    weights[(center, node)] = weights[(center, neighbor)] + weights[(neighbor, node)]
                    weights[(node, center)] = weights[(center, neighbor)] + weights[(neighbor, node)]
                    paths[(center, node)] = [neighbor] + paths[(neighbor, node)]
                    paths[(node, center)] = paths[(node, neighbor)] + [center]

    # for pair in itertools.combinations(vertices, 2):
    #     # distance vector algorithm dx(y) = min {c(x,v) + dv(y)}
    #     node1 = pair[0]
    #     node2 = pair[1]
    #     if node1 != node2:
    #         if (node1, node2) not in weights:
    #             weights[(node1, node2)] = float('inf')
    #         for neighbor in edges[node1]:
    #             if neighbor != node2 and (neighbor, node2) in weights and weights[(node1, node2)] > weights[(node1, neighbor)] + weights[(neighbor, node2)]:
    #                 weights[(node1, node2)] = weights[(node1, neighbor)] + weights[(neighbor, node2)]
    #                 weights[(node2, node1)] = weights[(node1, neighbor)] + weights[(neighbor, node2)]
    #                 paths[(node1, node2)] = [neighbor] + paths[(neighbor, node2)]
    #                 paths[(node2, node1)] = paths[(node2, neighbor)] + [node1]

        if center in edges[node]: # center is '3333'
            for neighbor in [_ for _ in edges[center] if _ != node]: # find neighbors of center, '4444' and '5555'
                #  if no existing node to center.neighbor or with greater distance
                if neighbor not in edges[node] or weights[(node, neighbor)] > weights[(node, center)] + weights[(center, neighbor)]:
                    weights[(node, neighbor)] = weights[(node, center)] + weights[(center, neighbor)]
                    weights[(neighbor, node)] = weights[(node, center)] + weights[(center, neighbor)]
                    paths[(node, neighbor)] = paths[(node, center)] + [neighbor]
                    paths[(neighbor, node)] = [center] + paths[(center, node)]
                if node not in edges[center] or weights[(center, node)] > weights[(center, neighbor)] + weights[(neighbor, node)]:
                    weights[(center, node)] = weights[(center, neighbor)] + weights[(neighbor, node)]
                    weights[(node, center)] = weights[(center, neighbor)] + weights[(neighbor, node)]
                    paths[(center, node)] = paths[(center, neighbor)] + [node]
                    paths[(node, center)] = [neighbor] + paths[(neighbor, node)]

# main function
print "==================================================="
print "\nCS6543 Link State Routing Simulator\n"
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
        f = open('data.txt', 'r')  # read data from file and write into matrix
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

