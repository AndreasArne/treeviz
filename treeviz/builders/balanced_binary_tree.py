"""
Uses invisible nodes to balances trees in graph.
Based on https://stackoverflow.com/a/48198645 to balance tree.
"""
from treeviz.builders.vertex import Vertex
from treeviz.builders.edge import Edge

class BalancedBinaryTreeGraph():
    """
    Builder for Balanced Binary Trees with igraph
    """
    _graph_type = "digraph"

    def __init__(self, node):
        if node is None:
            raise ValueError("Tree is empty, can't build Graph")

        # used to give unique id to invis nodes
        self.invis_counter = 0
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
            raise KeyError(f"Graph already contain vertex {name}.")
            
        self.vertexes[name] = Vertex(name, **kwargs)



    def _add_node_to_graph(self, node):
        """
        Recutsivly add tree node to the graph.
        Adds invisible nodes to balance vizualization of the tree.
        """
        key = node.key
        # key = str(node.key)
        # add node to graph
        self._add_vertex(name=key, label=key)

        if node.has_parent():
            self._add_edge(key, node.parent.key, "parent")

        if node.has_left_child():
            self._add_node_to_graph(node.left)
            self._add_edge(key, node.left.key, "left")
        else:
            self._add_invis_node(key)

        # add middle invis node. Too push the real nodes left and right.
        self._add_invis_node(key)

        if node.has_right_child():
            self._add_node_to_graph(node.right)
            self._add_edge(key, node.right.key, "right")
        else:
            self._add_invis_node(key)



    def _add_edge(self, src, dest, direction):
        """
        Try to add edge between two nodes.
        If it can't add edge, because a node is missing, it will add the missing node
        and an edge between them.
        """
        if src not in self.vertexes:
            raise ValueError(f"Missing the source key, {src}, from tree in graph. This shouldn't be possible!")
        if dest not in self.vertexes:
            print(
"Something is wrong. Can't add an edge between nodes \
'{first}' and '{second}'. Will add anyway to show structure. \
'{second}' probably doesn't exist in tree but '\
{first}' is referencing it. The error node will have color red".format(
                    first=src, second=dest
                )
            )
            self._add_vertex(
                name=dest,
                label=dest,
                color="red",
            )

            self.edges.append(Edge(
                self.vertexes[src].id,
                self.vertexes[dest].id,
                label=direction,
                color="red",
            ))
            return

        self.edges.append(Edge(
            self.vertexes[src].id,
            self.vertexes[dest].id,
        ))



    def _add_invis_node(self, key):
        """
        Add invis nodes to balance the tree.
        Need to set a weight, otherwise it gets weird.
        https://www.graphviz.org/doc/info/attrs.html#d:weight
        Don't really understand what it does/how it works.
        """
        self.invis_counter += 1
        inv_key = "i" + str(self.invis_counter)
        self._add_vertex(inv_key, label=inv_key, style="invis")

        self.edges.append(Edge(
            self.vertexes[key].id,
            self.vertexes[inv_key].id,
            style="invis",
            weight=5
        ))
