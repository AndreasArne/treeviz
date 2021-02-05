"""
Make treevizer a package.
Builds the public api with __all__.

Follows semantic versioning, https://semver.org/spec/v2.0.0.html
Given a version number MAJOR.MINOR.PATCH, increment the:

    MAJOR version when you make incompatible API changes,
    MINOR version when you add functionality in a backwards compatible manner, and
    PATCH version when you make backwards compatible bug fixes.
"""
from treevizer.main import tree_to_dot, tree_to_png, dot_to_png


__version__ = "0.0.8"

# what is __all__ https://stackoverflow.com/a/35710527
__all__ = [
    "tree_to_dot",
    "tree_to_png",
    "dot_to_png",
]
