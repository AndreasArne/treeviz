"""
Contain Edge class for use in a graph
"""
class Edge():
    """
    Edge class
    """
    def __init__(self, src, dest, **options):
        self.src = src
        self.dest = dest
        self.options = options



    def __repr__(self):
        options = "\n".join(
            [f"  {key}={value}" for key, value in self.options.items()]
        )

        repr = "{src} -> {dest} [\n{options}\n];".format(
            src=self.src,
            dest=self.dest,
            options=options,
        )
        return repr



    def __eq__(self, other):
        if other == (self.src, self.dest):
            return True
        return False



    def __contains__(self, other):
        print(other)
        return True if other == self.src or other == self.dest else False



if __name__ ==  "__main__":
    l = [
        Edge("1", "2", label="ko"),
        Edge("2", "1", label="haj", style="fixed"),
        Edge("3", "1"),
    ]
    # print("1" in l)
    print("\n".join([str(k) for k in l]))
