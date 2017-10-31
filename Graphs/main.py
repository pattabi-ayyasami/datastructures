from graph import Graph

def main():
    g = {"a": ["d"],
         "b": ["c"],
         "c": ["b", "c", "d", "e"],
         "d": ["a", "c"],
         "e": ["c"],
         "f": []
         }

    g = Graph(g)
    print g

    g.add_vertex("z")
    g.add_vertex("e")

    g.add_edge("z", "a")
    g.add_edge("x", "y")

    print "Vertices of graph: "
    print g.vertices()

    print "Edges of graph: "
    print g.edges()

    path = g.find_path("b", "e")
    print "Path (b-e):", path

    print "Exiting Graph(s) client program"

if __name__ == "__main__":
    main()