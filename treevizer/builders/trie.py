"""
Trie builder
"""
import html
from treevizer.builders.base_graph import Graph


class Trie(Graph):
    """
    Builder for Trie structure
    """

    def _add_node_to_graph(self, node, word=""):  # pylint: disable=arguments-differ
        """
        Recutsivly add tree node to the graph.
        """
        value = str(node.value)
        word += value
        children = node.children

        if node.stop:
            self._add_vertex(
                name=word,
                label=value,
                html_xlabel=self.create_xlabel(word),
                fillcolor="forestgreen",
                color="black",
            )
        else:
            self._add_vertex(name=word, label=value)

        if isinstance(children, list):
            self.add_children(children, word)
        elif isinstance(children, dict):
            self.add_children(children.values(), word)
        else:
            try:
                self.add_children(children, word)
            except TypeError as err:
                if "not iterable" in str(err):
                    # pylint: disable=raise-missing-from
                    raise TypeError(
                        (
                            "Datastructure for a nodes children is not supported. "
                            "Use list, dict or other iterable datastructure."
                        )
                    )
                raise err

    @staticmethod
    def create_xlabel(word):
        """
        Hande html in xlabel for displaying full words next to
        nodes.
        """
        word = html.escape(word)
        return f'<FONT COLOR="grey25" POINT-SIZE="12">{word}</FONT>'

    def add_children(self, children, word):
        """
        Iter over children and add to graph.
        """
        for child in children:
            self._add_node_to_graph(child, word)
            self._add_edge(word, word + child.value)
