"""
Entrypoint for module
Visualize tree datastructures.
"""
from treevizer.exporters import dot, png
from treevizer.builders.balanced_binary_tree import BalancedBinaryTreeGraph as bbt
from treevizer.builders.linked_list import LinkedListGraph as ll

AVAILABLE_TREES = "balanced binary tree (bbt), linked list (ll)"

def tree_to_dot(root, tree_type="bbt", filename="tree.dot"):
    """
    Create a dot file from tree datastructure
    """
    if root is None:
        raise ValueError("Tree is empty, cant vizualize empty trees!")


    if tree_type == "bbt":
        g = bbt(root)
    elif tree_type == "ll":
        g = ll(root)
    else:
        raise ValueError("We don't yet support that datastructre. Choose from {}."\
            .format(
                AVAILABLE_TREES
            ))

    dot.to_dot(g, filename)



def tree_to_png(root, graph, dotfile="tree.dot", pngfile="tree.png"):
    """
    Creates dot-file and png from tree structure
    """
    tree_to_dot(root, graph, dotfile)
    png.create_png(dotfile, pngfile)



def dot_to_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Creates png from dot file.
    """
    png.create_png(dotfile, pngfile)
