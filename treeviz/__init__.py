"""
Make treeviz a package.
Builds the public api with __all__.
"""
from treeviz.main import tree_to_dot, tree_to_png, dot_to_png

# what is __all__ https://stackoverflow.com/a/35710527
__all__ = [
    "tree_to_dot",
    "tree_to_png",
    "dot_to_png",
]
