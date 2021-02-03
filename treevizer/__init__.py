"""
Make treevizer a package.
Builds the public api with __all__.
"""
from treevizer.main import tree_to_dot, tree_to_png, dot_to_png

__version__ = "0.0.5"

# what is __all__ https://stackoverflow.com/a/35710527
__all__ = [
    "tree_to_dot",
    "tree_to_png",
    "dot_to_png",
]
