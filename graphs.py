class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex):
        if vertex not in self.vertices:
            self.vertices[vertex] = []

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            self.vertices[vertex1].append(vertex2)
            self.vertices[vertex2].append(vertex1)

    def remove_vertex(self, vertex):
        if vertex in self.vertices:
            del self.vertices[vertex]
            for v in self.vertices:
                if vertex in self.vertices[v]:
                    self.vertices[v].remove(vertex)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.vertices and vertex2 in self.vertices:
            if vertex2 in self.vertices[vertex1]:
                self.vertices[vertex1].remove(vertex2)
            if vertex1 in self.vertices[vertex2]:
                self.vertices[vertex2].remove(vertex1)

    def dfs(self, start_vertex):
        visited = set()
        stack = [start_vertex]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                stack.extend(self.vertices[vertex] - visited)

    def bfs(self, start_vertex):
        visited = set()
        queue = [start_vertex]

        while queue:
            vertex = queue.pop(0)
            if vertex not in visited:
                visited.add(vertex)
                print(vertex)
                queue.extend(self.vertices[vertex] - visited)


# Example usage of a graph

graph = Graph()

# Add vertices
graph.add_vertex('A')
graph.add_vertex('B')
graph.add_vertex('C')
graph.add_vertex('D')
graph.add_vertex('E')

# Add edges
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'E')

# Traverse the graph using DFS
print("Depth-First Search:")
graph.dfs('A')

# Traverse the graph using BFS
print("Breadth-First Search:")
graph.bfs('A')