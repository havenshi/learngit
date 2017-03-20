# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        return self.clone(node, dict={})

    def clone(self, node, dict):
        if node == None:
            return None
        if node.label in dict:
            return dict[node.label]
        root = UndirectedGraphNode(node.label)
        dict[node.label] = root
        for item in node.neighbors:
            root.neighbors.append(self.clone(item, dict))
        return root