# Graphs
# A graph is a set of vertices and the edges that connect those vertices. 
# All trees are graphs, but not all graphs are trees.
# https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/0qOGZwo.png

# LockedIn, like all social networks, has a social graph: each user is a vertex, and each "friendship" (or in corpo-speak "connection") is an edge. We want to represent this graph as a matrix. Our users each have a unique ID, which is an integer that we'll use for their vertex number.
    # Complete the __init__ method.
    # Create a new data member called graph, it should be an empty list.
    # Fill the graph with n lists, where n is the number of vertices in the graph.
    # Each of these lists should contain n False values.

class Graph:
    def __init__(self, num_vertices):
        self.graph = [[False] * num_vertices for _ in range(num_vertices)]

    def add_edge(self, u, v):
        self.graph[u][v] = True
        self.graph[v][u] = True

    # don't touch below this line

    def edge_exists(self, u, v):
        if u < 0 or u >= len(self.graph):
            return False
        if len(self.graph) == 0:
            return False
        row1 = self.graph[0]
        if v < 0 or v >= len(row1):
            return False
        return self.graph[u][v]

# Adjacency List
# Let's rebuild our graph using an adjacency list.
# An adjacency list stores a list of vertices for each vertex that indicates where the connections are.

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = set()
        self.graph[u].add(v)

        if v not in self.graph:
            self.graph[v] = set()
        self.graph[v].add(u)

    # don't touch below this line

    def edge_exists(self, u, v):
        if u in self.graph and v in self.graph:
            return (v in self.graph[u]) and (u in self.graph[v])
        return False

# Challenge 1 - Adjacent Nodes
    def adjacent_nodes(self, node):
        return list(self.graph.get(node, []))
        
# Challenge 2 - Unconnected Vertices
