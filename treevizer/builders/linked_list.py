"""
Contain class for building graph structure for linked list.
"""
from treevizer.builders.base_graph import Graph


class LinkedList(Graph):
    """
    Builder for Linked lists graph
    """

    def _add_node_to_graph(self, node):
        """
        Recutsivly add node to the graph.
        """
        label_template = "i={node_index}\\nv={value}"
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
