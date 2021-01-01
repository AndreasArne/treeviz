"""
Entrypoint for module
Visualize tree datastructures.
"""
from treeviz.exporters import dot, png
from treeviz.builders import balanced_binary_tree as bbt# , tree

AVAILABLE_TREES = "balanced binary tree (bbt), tree"

def tree_to_dot(root, tree_type="tree", filename="tree.dot"):
    """
    Create a dot file from tree datastructure
    """
    if root is None:
        raise ValueError("Tree is empty, cant vizualize empty trees!")


    if tree_type == "bbt":
        bbt.add_node_to_graph(root, g)
    elif tree_type == "tree":
        pass
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
