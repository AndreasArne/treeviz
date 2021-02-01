"""
Exports graph to dot file.
"""
from treevizer import config

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



def create_config_str(graph_type):
    """
    Create config string for dot file graph.
    """
    dot_config = config.get_config(graph_type)

    config_str = ""
    for graph_part, values in dot_config.items():
        options = [f"  {key}={value}" for key, value in values.items()]
        config_str += graph_part + " [\n" + ",\n".join(options) + "\n];\n"
    return config_str



def build_string(graph):
    """
    Create string with dot code from graph
    """
    graph_settings = create_config_str(graph.__class__.__name__)
    nodes = "\n".join([repr(vertex) for vertex in graph.vertexes.values()])
    edges = "\n".join([repr(edge) for edge in graph.edges])

    dot_string = "{graph_type} {{\n{config}\n{nodes}\n{edges}\n}}".format(
        graph_type=graph.graph_type(),
        config=graph_settings,
        nodes=nodes,
        edges=edges,
    )
    return dot_string
