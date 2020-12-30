"""
Exports graph to dot file.
"""
import json

config_filename = ".dot.json"

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



def create_config(graph_type, filename=config_filename):
    """
    Create config string for dot file graph.
    """
    with open(filename) as fd:
        config_json = json.load(fd)

    config = ""
    for graph_part, values in config_json[graph_type].items():
        options = [f"  {key}={value}" for key, value in values.items()]
        config += graph_part + " [\n" + ",\n".join(options) + "\n];\n"
    return config



def build_string(graph):
    """
    Create string with dot code from graph
    """
    graph_settings = create_config(graph.__class__.__name__)
    nodes = "\n".join([repr(vertex) for vertex in graph.vertexes.values()])
    edges = "\n".join([repr(edge) for edge in graph.edges])

    dot_string = "{graph_type} {{\n{config}\n{nodes}\n{edges}\n}}".format(
        graph_type=graph._graph_type,
        config=graph_settings,
        nodes=nodes,
        edges=edges,
    )
    return dot_string
