"""
Contain class for building graph structure for linked list.
"""
from treeviz.builders.vertex import Vertex
from treeviz.builders.edge import Edge

class LinkedListGraph():
    """
    Builder for Linked lists graph
    """
    _graph_type = "digraph"

    def __init__(self, node):
        if node is None:
            raise ValueError("List is empty, can't build Graph")

        # used to give unique id to invis nodes
        self.vertexes = {}
        self.edges = []
        self._add_node_to_graph(node)



    @property
    def graph_type(self):
        """
        return private variable
        """
        return self._graph_type



    def _add_vertex(self, name, **kwargs):
        """
        Take all arguments and add as options to vertex
        """
        if name in self.vertexes:
            breakpoint()
            raise KeyError(f"Graph already contain vertex {name}.")

        self.vertexes[name] = Vertex(name, **kwargs)



    def _add_node_to_graph(self, node):
        """
        Recutsivly add node to the graph.
        """
        label_template = '"i={node_index}\nv={value}"'
        node_index = 0
        value = node.data

        label = label_template.format(node_index=node_index, value=value)
        self._add_vertex(name=node_index, label=label)
        while node.next is not None:
            node = node.next
            value = node.data
            node_next_index = node_index + 1
            label = label_template.format(node_index=node_next_index, value=value)

            self._add_vertex(name=node_next_index, label=label)
            self._add_edge(node_index, node_next_index)
            node_index = node_next_index



    def _add_edge(self, src, dest):
        """
        Try to add edge between two nodes.
        If it can't add edge, because a node is missing, it will add the missing node
        and an edge between them.
        """
        if src not in self.vertexes:
            raise ValueError(f"Missing the source key, {src}, from tree in graph. This shouldn't be possible!")
        if dest not in self.vertexes:
            print((
                f"Something is wrong. Can't add an edge between nodes"
                f"'{src}' and '{dest}'. Will add anyway to show structure."
                f"'{dest}' probably doesn't exist in tree but '"
                f"{src}' is referencing it. The error node will have color red"
            ))
            self._add_vertex(
                name=dest,
                label=dest,
                color="red",
            )

            self.edges.append(Edge(
                self.vertexes[src].id,
                self.vertexes[dest].id,
                color="red",
            ))
            return

        self.edges.append(Edge(
            self.vertexes[src].id,
            self.vertexes[dest].id,
        ))
