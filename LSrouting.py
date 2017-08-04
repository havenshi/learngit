import numpy as np
import collections
import os
from numpy import genfromtxt
import pandas as pd
import json

class Graph:
    def __init__(self):
        # initial values of V, E and W as empty list or dict
        self.vertices = []
        self.edges = {}
        self.weights = {}

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

        if (from_vertex, to_vertex) not in self.weights:  # add each path
            self.weights[(from_vertex, to_vertex)] = distance
        if (to_vertex, from_vertex) not in self.weights:
            self.weights[(to_vertex, from_vertex)] = distance

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    S = set()

    # distance is the map of shortest paths from start to each v
    # initial value is infinite, e.g.2222 node has map of {5555: inf, 4444: inf, 3333: inf, 2222: inf}
    distance = dict.fromkeys(list(graph.vertices), float('inf'))
    # record the previous distance
    previous = dict.fromkeys(list(graph.vertices), None)

    distance[start] = 0
    while S != set(distance.keys()):
        # v is the closest vertex not be visited yet
        v = min((set(distance.keys()) - S), key=distance.get)

        # for each neighbor w of v not in S
        for w in set(graph.edges[v]) - S:
            newdistance = distance[v] + graph.weights[(v, w)]  # algorithm D(v) = min( D(v), D(w) + c(w,v) )
            if newdistance < distance[w]:
                distance[w] = newdistance
                # set the previous neighbor to v
                previous[w] = v
        S.add(v)   # after traversal each v, add it into S

    # current 2222 has map of {5555: 6, 4444: 4, 3333: 3, 2222: 0}
    return (distance, previous)


def path(graph, start, end):
    # record the paths between from_vertex and from_vertex_vertex
    distance, previous = dijkstra(graph, start)

    path = []
    vertex = end
    while vertex:  # until no start vertex
        path.append(vertex)
        vertex = previous[vertex]
    path.reverse()  # don't forget to reverse the list
    paths = '->'.join([str(x) for x in path])
    return dijkstra(graph, start)[0][end], paths


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
            G.add_vertex(str(matrix[i][0]))
            for j in range(1, n):
                if matrix[i][j] != 0 and matrix[i][j] != -1:
                    G.add_edge(str(matrix[i][0]), str(matrix[j][0]), matrix[i][j])

        print 'The current network is:'
        print G

    elif command == 2:  # create network by inputting port numbers and cost and write into matrix
        n = len(matrix)

        port = input('node ')
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
                    table[i][j] = [path(G, start, end)[0],
                                            path(G, start, end)[1]]  # modify graph with the optimal solution

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

