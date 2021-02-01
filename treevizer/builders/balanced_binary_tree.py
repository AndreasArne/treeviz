"""
Uses invisible nodes to balances trees in graph.
Based on https://stackoverflow.com/a/48198645 to balance tree.
"""
from treevizer.builders.edge import Edge
from treevizer.builders.base_graph import Graph

class BalancedBinaryTreeGraph(Graph):
    """
    Builder for Balanced Binary Trees with igraph
    """

    def __init__(self, node):
        # used to give unique id to invis nodes
        self.invis_counter = 0
        super().__init__(node)



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
