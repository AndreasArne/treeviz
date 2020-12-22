"""
Uses invisible nodes to balances trees in graph.
Based on https://stackoverflow.com/a/48198645 to balance tree.
"""
from treeviz.builders.tree import TreeBuilder
from treeviz.builders.vertex import Vertex
from treeviz.builders.edge import Edge

class BalancedBinaryTreeGraph():
    """
    Builder for Balanced Binary Trees with igraph
    """
    def __init__(self, node):
        if node is None:
            raise ValueError("Tree is empty, can't build Graph")

        # used to give unique id to invis nodes
        self.invis_counter = 0
        self.vertexes = {}
        self.edges = []
        self._add_node_to_graph(node)



    def _add_vertex(self, name, **kwargs):
        """
        Take all arguments and add as options to vertex
        """
        if name in self.vertexes:
            # breakpoint()
            raise KeyError(f"Graph already contain vertex {name}.")
            
        self.vertexes[name] = Vertex(name, **kwargs)



    def _add_node_to_graph(self, node):
        """
        Recutsivly add tree node to the graph.
        Adds invisible nodes to balance the tree.
        """
        key = str(node.key)
        # add node to graph
        self._add_vertex(name=key, label=key, style="filled")

        if node.has_parent():
            self._add_edge(key, node.parent.key)

        if node.has_left_child():
            self._add_node_to_graph(node.left)
            self._add_edge(key, node.left.key)
        else:
            self._add_invis_node(key)

        # add middle invis node. Too push the real nodes left and right.
        self._add_invis_node(key)

        if node.has_right_child():
            self._add_node_to_graph(node.right)
            self._add_edge(key, node.right.key)
        else:
            self._add_invis_node(key)



    def _add_edge(self, key, other_key):
        """
        Try to add edge between two nodes.
        If it can't add edge, because a node is missing, it will add the missing node
        and an edge between them.
        """
        other_key = str(other_key)
        if key not in self.vertexes:
            raise ValueError(f"Missing the source key, {key}, from tree in graph. This shouldn't be possible!")
        if other_key not in self.vertexes:
            print(
"Something is wrong. Can't add an edge between\
{first} and {second}. Will add anyway to show structure.\
{second} probably doesn't exist in tree but\
{first} is referencing it.".format(
                    first=key, second=other_key
                )
            )
            self._add_vertex(
                name=str(other_key),
                label=str(other_key),
                style="filled",
            )

        self.edges.append(Edge(
            self.vertexes[key].id,
            self.vertexes[str(other_key)].id,
            style="filled",
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
