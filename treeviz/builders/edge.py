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
            [f'  {key}="{value}"' for key, value in self.options.items()]
        )

        repr_ = "{src} -> {dest} [\n{options}\n];".format(
            src=self.src,
            dest=self.dest,
            options=options,
        )
        return repr_



    def __eq__(self, other):
        return other == (self.src, self.dest)



    def __contains__(self, other):
        return other in (self.src, self.dest)



if __name__ == "__main__":
    l = [
        Edge("1", "2", label="ko"),
        Edge("2", "1", label="haj", style="fixed"),
        Edge("3", "1"),
    ]
    # print("1" in l)
    print("\n".join([str(k) for k in l]))
