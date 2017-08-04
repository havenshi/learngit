import numpy as np
import collections
import os

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
        self.weights[(from_vertex, to_vertex)] = distance  # add each path

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
# create network by inputting port numbers and cost and write into matrix
n = input("Enter how many nodes you want: ")  # define the port number

G = Graph()
for i in range(n):
    port = input('node ')
    G.add_vertex(port)
    for j in range(n):
        neighbor, cost = input('Enter neighbors (neighbor and cost with a comma in between): ')
        if neighbor == -1 and cost == -1:  # exit input, jump out of the loop
            break
        else:
            G.add_vertex(neighbor)
            G.add_edge(port, neighbor, cost)
    print G  #  after a new node added to the network, print the current view of the network at the node


# store shortest cost from node to node and its path into a routing table
matrix = [[-1] * n for _ in range(n)]
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            matrix[i - 1][i -1 ] = 0  # the cost from node to itself is 0
        else:
            start = G.vertices[i - 1]
            end = G.vertices[j - 1]
            matrix[i - 1][j - 1] = [path(G, start, end)[0], path(G, start, end)[1]]  # modify graph with the optimal solution
for i in range(n):
    print matrix[i]


# generate routing table
for i in range(n):
    print 'Routing table at node %s' % (G.vertices[i])
    print 'Destination' + '\t' + 'Next Node' + '\t' + 'Cost'
    for j in range(n):
        if j != i:  # extract path and cost from each node
            paths = matrix[i][j][1].split('->')  # next node is the second node from the start node
            print str(G.vertices[j]) + '\t' + paths[1] + '\t' + str(matrix[i][j][0])
