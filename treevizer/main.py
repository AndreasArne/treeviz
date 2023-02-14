"""
Entrypoint for module
Visualize tree datastructures.
"""
from functools import update_wrapper
from treevizer.exporters import dot, png, gif
from treevizer.builders.balanced_binary_tree import BalancedBinaryTree as bbt
from treevizer.builders.linked_list import LinkedList as ll
from treevizer.builders.trie import Trie as trie
from treevizer.builders.recursion import Recursion

AVAILABLE_TREES = "balanced binary tree (bbt), linked list (ll), trie (trie)"
decorated_functions = {}


def recursion_to_gif(function_name, gif_path="recursion.gif", duration=800, loop=0):
    """
    Use name of function as key to chose which graph to render.
    Duration in miliseconds.
    Loop: 0 = infinity, above is how many time to loop after 1 loop.
    """
    # pylint: disable=raise-missing-from
    try:
        decorated_function = decorated_functions[function_name]
    except KeyError:
        raise ValueError(f"No decorated function with the name {function_name} exist.")
    gif.to_gif(decorated_function, gif_path, duration, loop)


def recursion_to_png(function_name, dot_path="recursion.dot", png_path="recursion.png"):
    """
    Use name of function as key to chose which graph to render
    """
    # pylint: disable=raise-missing-from
    try:
        decorated_function = decorated_functions[function_name]
    except KeyError:
        raise ValueError(f"No decorated function with the name {function_name} exist.")
    dot.to_dot(decorated_function, dot_path)
    png.create_png(dot_path, png_path)


def recursion_viz(fn):
    """
    Intermediare function for Recursion class.
    Use this to save Recursion object to make it possible to decorate more than 1 function.
    """
    decorator = Recursion(fn)
    update_wrapper(decorator, fn)
    decorated_functions[fn.__name__] = decorator
    return decorator


def to_dot(root, structure_type="bbt", dot_path="tree.dot"):
    """
    Create a dot file from tree datastructure
    """
    if root is None:
        raise ValueError("Tree is empty, cant vizualize empty trees!")

    if structure_type == "bbt":
        g = bbt(root)
    elif structure_type == "ll":
        g = ll(root)
    elif structure_type == "trie":
        g = trie(root)
    else:
        raise ValueError(
            f"We don't yet support that datastructre. Choose from {AVAILABLE_TREES}."
        )

    dot.to_dot(g, dot_path)


def to_png(root, structure_type="bbt", dot_path="tree.dot", png_path="tree.png"):
    """
    Creates dot-file and png from tree structure
    """
    to_dot(root, structure_type, dot_path)
    png.create_png(dot_path, png_path)


def dot_to_png(dot_path="tree.dot", png_path="tree.png"):
    """
    Creates png from dot file.
    """
    png.create_png(dot_path, png_path)
