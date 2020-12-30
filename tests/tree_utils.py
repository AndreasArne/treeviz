"""
Contains utility functions for testing a Binary Search Tree
"""
import random
random.seed("BST")

def random_seq(n):
    """Creat a list with random values from range"""
    return random.sample(range(n), n)

def random_seq_from_list(l):
    """Creat a list with random values from list"""
    return random.sample(l, len(l))

def shuffle(arr):
    """Shuffle an array"""
    random.shuffle(arr)

def get_nodes_neighbors(node):
    """
    Iterate through tree and yield a list containing
    a nodes key, parent, left and right
    Yields in recursive function https://www.python.org/dev/peps/pep-0380/
    by creating subgenerators
    """
    yield [
        node.key,
        node.parent.key if node.parent else None,
        node.left.key if node.left else None,
        node.right.key if node.right else None,
    ]
    if node.has_left_child():
        yield from get_nodes_neighbors(node.left)
    if node.has_right_child():
        yield from get_nodes_neighbors(node.right)



def list_to_bst(seq, bst):
    """
    Take list and insert value in BST.
    Using values from list as keys and index from list as values in BST.
    """
    for v, k in enumerate(seq):
        bst.insert(k, v)

def list_to_dict(seq):
    """
    Take list and insert value in dict
    Using values from list as keys and index from list as values in BST.
    """
    d = {}
    for v, k in enumerate(seq):
        d[k] = v
    return d
