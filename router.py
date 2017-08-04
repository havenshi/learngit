import collections

class Graph:
    def __init__(self):
        # initial values of V, E and W as empty list or dict
        self.vertices = set()
        self.edges = collections.defaultdict(list)
        self.weights = {}

    def add_vertex(self, value):
        self.vertices.add(value)

    def add_edge(self, from_vertex, to_vertex, distance):
        # from and to vertices are different, and there's path between them
        if matrix[from_vertex - 1][to_vertex - 1] != -1 and matrix[from_vertex - 1][to_vertex - 1] != 0:
            if from_vertex in self.edges:  # add edges of one node into map
                self.edges[from_vertex].append(to_vertex)
            else:
                self.edges[from_vertex] = [to_vertex]
            self.weights[(from_vertex, to_vertex)] = distance  # add each path

    def __str__(self):
        string = "Vertices: " + str(self.vertices) + "\n"
        string += "Edges: " + str(self.edges) + "\n"
        string += "Weights: " + str(self.weights)
        return string


def dijkstra(graph, start):
    S = set()

    # distance is the map of shortest paths from start to each v
    # initial value is infinite, e.g.2222 vertex has map of {5555: inf, 4444: inf, 3333: inf, 2222: inf}
    distance = dict.fromkeys(list(graph.vertices), float('inf'))
    # record the previous distance
    previous = dict.fromkeys(list(graph.vertices), None)

    distance[start] = 0
    while S != graph.vertices:
        # v is the closest vertex not be visited yet
        print distance
        v = min((set(distance.keys()) - S), key = distance.get)

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
    return 'shortest distance from ' + str(start) + ' to ' + str(end) + ': ' + str(dijkstra(graph, end)[0][start]) + '\n' + 'shortest path: ' + paths


# main function
matrix = []
with open('data.txt', 'r') as f:
    matrix = [list(map(int, x.split(" "))) for x in f]  # read data from file and write into matrix
print matrix
G = Graph()
n = len(matrix)
for i in range(1, n + 1):
    G.add_vertex(i)
    for j in range(1, n + 1):
        G.add_edge(i, j, matrix[i - 1][j - 1])

    # after add each node into graph, print node map
    print 'node ' + str(i) + '\n' + 'Enter neighbors:'
    for j in G.edges[i]:
        print str(i) + '  ' + str(matrix[i - 1][j - 1])
    print '-1  -1'

start = input('please input start vertex:')
end = input('please input start vertex:')

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if matrix[i - 1][j - 1] != 0:
            G.weights[(i, j)] = dijkstra(G, j)[0][i]  # modify graph with the optimal solution

print(path(G, start, end))
print G