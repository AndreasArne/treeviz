"""
Exports igraph tree to dot file.
"""
import re
def to_dot(graph, filename="tree.dot"):
    """
    Use igraph to write dot file and insert global graphviz settings in file.
    """
    graph.write_dot(filename)
    insert_graph_settings(filename)



def insert_graph_settings(filename):
    """
    Use regex to inject global settings in dot file.
    """
    with open(filename, "r") as fh:
        content = fh.read()
    pattern = r"(digraph {)"
    settings = """
      graph[nodesep=0.25, ranksep=0.3, splines=line];
      node [
        style=filled, fillcolor=lightblue,
        shape=circle, fixedsize=true, width=0.5];
        edge [arrowsize=0.8];
    """
    repl = "\g<1>{}\n".format(settings)
    new_content = re.sub(pattern, repl, content)
    with open(filename, "w") as fh:
        fh.write(new_content)