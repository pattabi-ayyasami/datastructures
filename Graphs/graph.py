

class Graph:

    def __init__(self, graph_dict = None):
        if graph_dict is None:
            self.graph_dict = {}
        else:
            self.graph_dict = graph_dict

    def vertices(self):
        return self.graph_dict.keys()

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []
        else:
            print "Vertex '%s' already in graph" %vertex

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph_dict:
            self.graph_dict[vertex1].append(vertex2)
        else:
            self.graph_dict[vertex1] = [vertex2]

    def __generate_edges(self):
        edges = []
        for vertex in self.graph_dict:
            neighbors = self.graph_dict[vertex]
            for neighbor in neighbors:
                if {neighbor, vertex} not in edges:
                    edges.append({vertex, neighbor})
        return edges

    def find_path(self, start_vertex, end_vertex, path = None):
        if path is None:
            path = []

        if start_vertex not in self.graph_dict:
            return None

        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return path

        connected_vertices = self.graph_dict[start_vertex]
        for vertex in connected_vertices:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def __str__(self):
        result = "Vertices: "
        for v in self.graph_dict:
            result += v + " "

        result += "\nEdges: "
        edges = self.__generate_edges()
        for edge in edges:
            result += str(edge) + " "

        return result