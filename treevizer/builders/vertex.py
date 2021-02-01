"""
Contain Vertex class for use in a graph
"""
class Vertex():
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



    def __repr__(self):
        repr_ = "{} [\n  {}\n];".format(
            self._id,
            "\n  ".join(
                [f'{key}="{value}"'for key, value in self.options.items()]
            )
        )
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
