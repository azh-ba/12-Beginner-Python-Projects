import random

class Vertex:
    def __init__(self, value):
        self.value = value
        self.adjacent = {}
        self.neighbors = []
        self.neighbors_weight = []

    def add_edge_to(self, vertex, weight = 0):
        """Adding an edge with weight to the vertex input."""
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        """Incrementing the weight of the edge."""
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def get_probability_map(self):
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weight.append(weight)

    def next_word(self):
        """Randomly select next word based on weights."""
        return random.choices(self.neighbors, weights=self.neighbors_weight)[0]


class Graph:
    def __init__(self):
        self.vertices = {}
    
    def get_vertex_values(self):
        """Return all possible words."""
        return set(self.vertices.keys())
    
    def add_vertex(self, value):
        """Add a new vertex to the graph."""
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        """Get the vertex object."""
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]
    
    def get_next_word(self, current_vertex):
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        for vertex in self.vertices.values():
            vertex.get_probability_map()