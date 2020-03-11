"""
# TODO: Builder for Trie. No need to balance it.

Builds trees with igraph.
igraph - pip3 install python-igraph
Uses invisible nodes to balances trees.
Based on https://stackoverflow.com/a/48198645 to balance tree.
"""
from igraph import Graph

class TreeBuilder():
    """
    Class for building a tree with igraph
    """
    def __init__(self, node):
        if node is None:
            raise ValueError("Tree is empty cant build tree")

        self.graph = Graph(
            directed=True,
        )
        self._add_node_to_graph(node)



    def _add_node_to_graph(self, node):
        """
        Recutsivly add tree node to the graph.
        Adds invisible nodes to balance the tree.
        """
        key = str(node.key)
        # add node to graph
        self.graph.add_vertex(name=key, label=key, style="filled")

        if node.has_parent():
            self.add_edge(key, node.parent.key)

        if node.has_left_child():
            self.add_node_to_graph(node.left)
            self.add_edge(key, node.left.key)
        else:
            self.add_invis_node(key)

        # add middle invis node. Too push the real nodes left and right.
        self.add_invis_node(key)

        if node.has_right_child():
            self.add_node_to_graph(node.right)
            self.add_edge(key, node.right.key)
        else:
            self.add_invis_node(key)



    def _add_edge(self, key, other_key):
        """
        Try to add edge between two nodes.
        If it can't add edge, because a node is missing, it will add the node
        and and edge between them.
        """
        try:
            self.graph.add_edge(key, str(other_key), style="filled")
        except ValueError:
            print(
                "Something is wrong. Can't add an edge between\
 {first} and {second}. Will add anyway to show structure.\
 {second} probably doesn't exist in tree but\
 {first} is referencing it.".format(
                    first=key, second=other_key
                )
            )
            self.graph.add_vertex(
                name=str(other_key),
                label=str(other_key),
                style="filled",
            )
            self.graph.add_edge(key, str(other_key), style="filled")
