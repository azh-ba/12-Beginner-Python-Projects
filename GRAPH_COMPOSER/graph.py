import random

class Vertex:
    def __init__(self, value):
        """Constructor for vertex."""
        # value (word) of a vertex
        self.value = value

        # a dict of vertices adjacent to it, follow by the weight of the edge
        self.adjacent = {}

        # a list of vertices adjacent to it
        self.neighbors = []

        # a list of edge weights associated with the adjacent vertices
        self.neighbors_weight = []

    def add_edge(self, vertex, weight = 0):
        """Add a new edge to a vertex."""
        self.adjacent[vertex] = weight

    def increment_edge(self, vertex):
        """Increase the weight of a particular edge."""
        # if vertex does not have an edge, add a new edge with weight = 1
        self.adjacent[vertex] = self.adjacent.get(vertex, 0) + 1

    def probability_map(self):
        """Generate a probability map of a vertex."""
        for (vertex, weight) in self.adjacent.items():
            self.neighbors.append(vertex)
            self.neighbors_weight.append(weight)

    def next_word(self):
        """Get the next values (word)."""
        return random.choices(self.neighbors, weights=self.neighbors_weight)[0]

class Graph:
    def __init__(self):
        """Constructor for graph."""
        # a dict of vertices
        self.vertices = {}

    def get_vertex_values(self):
        """Get all values (word) in the graph."""
        return set(self.vertices.keys())

    def add_vertex(self, value):
        """Add a new vertex to the graph."""
        self.vertices[value] = Vertex(value)

    def get_vertex(self, value):
        """Return a vertex."""
        # if no vertex exists, add to the vertices dict
        if value not in self.vertices:
            self.add_vertex(value)
        return self.vertices[value]

    def get_next_word(self, current_vertex):
        """Return the next value (word)."""
        return self.vertices[current_vertex.value].next_word()

    def generate_probability_mappings(self):
        """Generate a probability map for each vertex of the graph."""
        for vertex in self.vertices.values():
            vertex.probability_map()