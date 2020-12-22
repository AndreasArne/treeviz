"""
Exports graph to dot file.
"""

def to_dot(graph, filename="tree.dot"):
    """
    Use igraph to write dot file and insert global graphviz settings in file.
    """
    string = build_string(graph)
    write_to_file(string, filename)



def write_to_file(content, filename):
    """
    Write string to file
    """
    with open(filename, "w") as fd:
        fd.write(content)



def build_string(graph):
    """
    Create string with dot code from graph
    """
    graph_settings = """digraph {
  graph[
    nodesep=0.25, ranksep=0.3, splines=line
  ];
  node [
    style=filled, fillcolor=lightblue,
    shape=circle, fixedsize=true, width=0.5
  ];
  edge [
    arrowsize=0.8
  ];
  """
    nodes = "\n".join([repr(vertex) for vertex in graph.vertexes.values()])
    edges = "\n".join([repr(edge) for edge in graph.edges])

    dot_string = "{start}\n{nodes}\n{edges}\n}}".format(
        start=graph_settings,
        nodes=nodes,
        edges=edges,
    )
    return dot_string
