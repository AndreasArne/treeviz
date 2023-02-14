"""
Contain class for base class for other builders.
"""
from treevizer.builders.vertex import Vertex
from treevizer.builders.edge import Edge


class Graph:
    """
    Builder for base graphs. Other graphs should inherit from this class.
    """

    _graph_type = "digraph"

    def __init__(self, node):
        if node is None:
            raise ValueError("Node is empty, can't build Graph")

        self.vertexes = {}
        self.edges = []
        self._add_node_to_graph(node)

    @classmethod
    def graph_type(cls):
        """
        return private variable
        """
        return cls._graph_type

    def _add_vertex(self, name, **kwargs):
        """
        Take all arguments and add as options to vertex
        """
        if name in self.vertexes:
            raise KeyError(f"Graph already contain vertex {name}.")

        self.vertexes[name] = Vertex(name, **kwargs)

    def _add_node_to_graph(self, node):
        """
        Add nodes to graph as vertexes and edges
        """
        raise NotImplementedError("Subclasses must implement this!")

    def _add_edge(self, src, dest, error_edge_label=None):
        """
        Try to add edge between two nodes.
        If it can't add edge, because a node is missing, it will add the missing node
        and an edge between them.
        """
        if src not in self.vertexes:
            raise ValueError(
                f"Missing the source key, {src}, from tree in graph. This shouldn't be possible!"
            )
        if dest not in self.vertexes:
            print(
                (
                    f"Something is wrong. Can't add an edge between nodes"
                    f"'{src}' and '{dest}'. Will add anyway to show structure."
                    f"'{dest}' probably doesn't exist in tree but '"
                    f"{src}' is referencing it. The error node will have color red"
                )
            )
            self._add_vertex(
                name=dest,
                label=dest,
                color="red",
            )

            self.edges.append(
                Edge(
                    self.vertexes[src].id,
                    self.vertexes[dest].id,
                    label=error_edge_label,
                    color="red",
                )
            )
            return

        self.edges.append(
            Edge(
                self.vertexes[src].id,
                self.vertexes[dest].id,
            )
        )
