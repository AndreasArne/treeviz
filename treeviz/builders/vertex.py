"""
Contain Vertex class for use in a graph
"""
class Vertex():
    """
    Vertex class
    """
    _id_counter = 0

    def __init__(self, name, **kwargs):
        self.name = name
        self.options = kwargs
        self.options["name"] = name
        self._id = Vertex._id_counter
        Vertex._id_counter += 1



    @property
    def id(self):
        return self._id



    def __repr__(self):
        repr = "{} [\n{}\n];".format(
            self._id,
            "\n  ".join(
                [f"{key}={value}" for key, value in self.options.items()]
            )
        )
        return repr



    def __str__(self):
        return repr(self)



    def __eq__(self, name):
        if str(name) == self.name:
            return True
        return False



if __name__ ==  "__main__":
    l = [
        Vertex("1", label="ko"),
        Vertex("2", label="haj", style="fixed"),
        Vertex("3"),
    ]
    # print("1" in l)
    print("\n".join([str(k) for k in l]))