# Breadth First Search (BFS)
# Breadth-first search (BFS) is an algorithm for traversing or searching tree or graph data structures. 
# It starts at a root (some arbitrary node on a graph), and explores all of the neighbor nodes at the present 
# depth before going on to the nodes at the next depth level.

class Graph:
    def breadth_first_search(self, v):
        visited = []
        to_visit = [v]
        while to_visit:
            vertex = to_visit.pop(0)
            if vertex not in visited:
                visited.append(vertex)
                neighbors = sorted(self.graph[vertex])

                for neighbor in neighbors:
                    if neighbor not in visited and neighbor not in to_visit:
                        to_visit.append(neighbor)

        return visited
    
# Depth First Search (DFS)
# Depth-first search (DFS) is just another algorithm to traverse a graph - kind of like breadth first search. 
# It starts at a root node (some arbitrary node on the graph) and explores as far as possible along each branch 
# before backtracking and starting down the next branch.

class Graph:
    def depth_first_search(self, start_vertex):
        visited = []
        self.depth_first_search_r(visited, start_vertex)
        return visited

    def depth_first_search_r(self, visited, current_vertex):
        visited.append(current_vertex)
        neighbors = sorted(self.graph[current_vertex])
        for neighbor in neighbors:
            if neighbor not in visited:
                self.depth_first_search_r(visited, neighbor)
        return visited
    
# Challenge 1 - Shortest Path
    def bfs_path(self, start, end):
        if start == end:
            return [start]
        visited = set()
        queue = [start]
        parent = {start: None}

        while queue:
            current_vertex = queue.pop(0)

            if current_vertex == end:
                path = []
                while current_vertex is not None:
                    path.append(current_vertex)
                    current_vertex = parent[current_vertex]
                return path [::-1]

            visited.add(current_vertex)
            
            for neighbor in self.graph.get(current_vertex, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
                    parent[neighbor] = current_vertex
        return None