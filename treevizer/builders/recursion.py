
"""
Contain class for visualizing recursive function calls.
"""
import html
from treevizer.builders.edge import Edge
from treevizer.builders.vertex import Vertex

class Recursion():
    """
    Class for visualizing recursive function calls.
    """
    _graph_type = "digraph"

    def __init__(self, fn):
        self._call_counter = 0
        self._edge_counter = 0
        self.vertexes = {}
        self.edges = []
        self._stack = []
        self._fn = fn



    @classmethod
    def graph_type(cls):
        """
        return private variable
        """
        return cls._graph_type



    def _create_fn_call_str(self, args, kwargs):
        """
        Build string with function name and args and kwargs.
        Also escape html characters so can be part of html-string for label
        """
        arg_kwargs_str_list = []
        if args:
            arg_kwargs_str_list.extend([repr(arg) for arg in args])
        if kwargs:
            arg_kwargs_str_list.extend([f"{str(k)}={repr(v)}" for k, v in kwargs.items()])
        arg_kwargs_str = ", ".join(arg_kwargs_str_list)
        return html.escape(f"{self._fn.__name__}({arg_kwargs_str})")



    def __call__(self, *args, **kwargs):
        """
        This is the wrapper function for the users recursive function
        """
        label_table = (
            '<TABLE BORDER="0" CELLBORDER="0" CELLSPACING="0">'
            '<TR><TD>{call}</TD></TR>'
            '<HR/>'
            '<TR><TD>{ret}</TD></TR>'
            '</TABLE>'
        )
        # create vertex
        label_table = label_table.replace("{call}", self._create_fn_call_str(args, kwargs))
        self.vertexes[self._call_counter] = Vertex(self._call_counter, html_label=label_table)

        # create call edge
        if self._call_counter > 0:
            self._edge_counter += 1
            self.edges.append(Edge(
                self.vertexes[self._stack[-1]].id,
                self.vertexes[self._call_counter].id,
                label=f"#{self._edge_counter}"
            ))

        # add current NR to stack
        self._stack.append(self._call_counter)
        # Increase fpr next call
        self._call_counter += 1
        # call function
        result = self._fn(*args, **kwargs)

        # get current NR for index
        call_indx = self._stack.pop()
        call_vertex = self.vertexes[call_indx]
        # update vertex with return value
        call_vertex.options["html_label"] = call_vertex.options["html_label"].format(
            ret=html.escape(f"return {result}")
        )

        # create return edge
        if call_indx > 0:
            self._edge_counter += 1
            self.edges.append(Edge(
                call_vertex.id,
                self.vertexes[self._stack[-1]].id,
                label=f"#{self._edge_counter}"
            ))

        return result
