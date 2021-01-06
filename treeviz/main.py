"""
Entrypoint for module
Visualize tree datastructures.
"""
from treeviz.exporters import dot, png
from treeviz.builders.balanced_binary_tree import BalancedBinaryTreeGraph as bbt# , tree

AVAILABLE_TREES = "balanced binary tree (bbt)"

def tree_to_dot(root, tree_type="bbt", filename="tree.dot"):
    """
    Create a dot file from tree datastructure
    """
    if root is None:
        raise ValueError("Tree is empty, cant vizualize empty trees!")


    if tree_type == "bbt":
        g = bbt(root)
    else:
        raise ValueError("We don't yet support that tree type. Choose from {}."\
            .format(
                AVAILABLE_TREES
            ))

    dot.to_dot(g, filename)



def tree_to_png(root, dotfile="tree.dot", pngfile="tree.png"):
    """
    Creates dot-file and png from tree structure
    """
    tree_to_dot(root, dotfile)
    png.create_png(dotfile, pngfile)



def dot_to_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Creates png from dot file.
    """
    png.create_png(dotfile, pngfile)
