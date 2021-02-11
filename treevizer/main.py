"""
Entrypoint for module
Visualize tree datastructures.
"""
from treevizer.exporters import dot, png
from treevizer.builders.balanced_binary_tree import BalancedBinaryTree as bbt
from treevizer.builders.linked_list import LinkedList as ll

AVAILABLE_TREES = "balanced binary tree (bbt), linked list (ll)"

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
    else:
        raise ValueError("We don't yet support that datastructre. Choose from {}."\
            .format(
                AVAILABLE_TREES
            ))

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
