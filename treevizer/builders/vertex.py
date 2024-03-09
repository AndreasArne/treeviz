"""
Contain Vertex class for use in a graph
"""
import copy


class Vertex:
    """
    Vertex class
    """

    def __init__(self, name, **kwargs):
        self.name = name
        self.options = kwargs
        self._id = id(name)

    @property
    def id(self):
        """
        return private attrbute
        """
        return self._id

    def _build_node_string(self):
        """
        Copy options to local variable. If html_label, we wont delete it completely from vertex, only the local version.
        """
        options = copy.deepcopy(self.options)
        node_list = []

        for key, value in options.items():
            if key.startswith("html_"):
                real_key = key.replace("html_", "")
                node_list.append(f"{real_key}=<" + value + ">")
            else:
                node_list.append(f'{key}="{value}"')

        return "\n  ".join(node_list)

    def __repr__(self):
        repr_ = f"{self._id} [\n  {self._build_node_string()}\n];"
        return repr_

    def __str__(self):
        return repr(self)

    def __eq__(self, name):
        return name == self.name


if __name__ == "__main__":
    l = [
        Vertex("1", label="ko"),
        Vertex("2", label="haj", style="fixed"),
        Vertex("3"),
    ]
    # print("1" in l)
    print("\n".join([str(k) for k in l]))
