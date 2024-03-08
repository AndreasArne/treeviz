"""
Contains code for a Binary Search Tree and Node
"""
import treevizer
class Person():
    """
    Clas can be ignored, only for testing
    """
    def __init__(self, name, ssn):
        self.name = name
        self._ssn = ssn
    def __repr__(self):
        return "name: {}, ssn: {}".format(self.name, self._ssn)

class Node():
    """
    Node class for a BST
    """
    def __init__(self, key, value, parent=None):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = parent

    def has_left_child(self):
        """ Check if has left child """
        return self.left is not None

    def has_right_child(self):
        """ Check if has right child """
        return self.right is not None

    def is_left_child(self):
        """ Check if is left child to parent """
        return self.parent is not None and self.parent.left == self

    def is_right_child(self):
        """ Check if is right child to parent """
        return self.parent is not None and self.parent.right == self

    def is_leaf(self):
        """ Check if is a leaf """
        return not (self.has_left_child() or self.has_right_child())

    def has_both_children(self):
        """ Check if has two children """
        return self.has_left_child() and self.has_right_child()

    def has_parent(self):
        """ Check if has parent node """
        return self.parent is not None

    def __repr__(self):
        # return "{}".format(self.key)
        return "key: {}, value: {}".format(self.key, self.value)
    def __lt__(self, other):
        if isinstance(other, Node):
            return self.key < other.key
        return self.key < other
    def __gt__(self, other):
        if isinstance(other, Node):
            return self.key > other.key
        return self.key > other
    def __eq__(self, other):
        if isinstance(other, Node):
            return self.key == other.key
        return self.key == other

class BinarySearchTree():
    """
    BST with nodes containing key and value
    """
    def __init__(self):
        self.size = 0
        self.root = None

    def insert(self, key, value):
        """ Insert Key/value pair """
        if self.root is None:
            self.root = Node(key, value)
        else:
            self._insert(key, value, self.root)

        self.size += 1

    @staticmethod
    def _insert(key, value, node):
        """ Helper method for insert, is recursive """
        if key < node:
            if node.has_left_child():
                BinarySearchTree._insert(key, value, node.left)
            else:
                node.left = Node(key, value, node)
        elif key > node:
            if node.has_right_child():
                BinarySearchTree._insert(key, value, node.right)
            else:
                node.right = Node(key, value, node)
        else:
            node.value = value

    def inorder_traversal_print(self):
        """ Print tree values in order """
        self._print_nodes(self.root)

    @staticmethod
    def _print_nodes(node):
        """ Helper method for inorder_traversal_print, is recursive """
        if node is None:
            return
        if node.has_left_child():
            BinarySearchTree._print_nodes(node.left)
        print(node.value)
        if node.has_right_child():
            BinarySearchTree._print_nodes(node.right)

    def get(self, key):
        """ Get a value from tree using key """
        if self.root is None:
            raise KeyError("Empty BST")
        result = self._get(key, self.root)
        return result.value

    @staticmethod
    def _get(key, node):
        """ Helper method for get, is recursive """
        if node is None:
            raise KeyError("No such key, {}".format(key))
        elif key == node:
            return node
        elif key < node:
            return BinarySearchTree._get(key, node.left)
        else:
            return BinarySearchTree._get(key, node.right)

    def remove(self, key):
        """ Remove key/value pair from tree with key """
        if self.root is None:
            raise KeyError("Empty BST")
        node_to_remove = self._get(key, self.root)
        ret_val = node_to_remove.value
        if node_to_remove.has_both_children():
            successor = self._inOrderSuccessor(node_to_remove.right)
            node_to_remove.value = successor.value
            node_to_remove.key = successor.key
            self._replace_node_parent(successor, successor.right)
        elif node_to_remove.has_left_child():
            self._replace_node_parent(node_to_remove, node_to_remove.left)
        elif node_to_remove.has_right_child():
            self._replace_node_parent(node_to_remove, node_to_remove.right)
        else:
            self._replace_node_parent(node_to_remove, None)
        self.size -= 1
        return ret_val

    @staticmethod
    def _inOrderSuccessor(node):
        """
        Helper method for remove, for finding min value in a tree.
        Is recursive
        """
        current = node
        while current.has_left_child():
            current = current.left
        return current

    def _replace_node_parent(self, node, child):
        """ Helper method for remove, is recursive """
        if node.has_parent():
            if node.is_left_child():
                node.parent.left = child
            else:
                node.parent.right = child
        else:
            self.root = child
        # If we dont do this, the nodes keep their old removed parent
        if child is not None:
            child.parent = node.parent



    def __setitem__(self, k, v):
        self.insert(k, v)
    def __getitem__(self, k):
        return self.get(k)
    def __contains__(self, k):
        try:
            self.get(k)
            return True
        except KeyError:
            return False


if __name__ == "__main__":
    bst = BinarySearchTree()
    bst["andreas"] = Person("andreas", 214412)
    bst["daniel"] = Person("daniel", 234214)
    bst["ko"] = Person("ko", 9872414)
    bst["apa"] = Person("apa", 735232)
    bst["koala"] = Person("koala", 538925)
    bst["persbrant"] = Person("persbrant", 353259)
    bst["boalt"] = Person("boalt", 89234)
    bst["najs"] = Person("najs", 35235)
    bst["palt"] = Person("palt", 546346)
    # print(bst["andreas"])
    bst.remove("andreas")


    root = Node(1, "1")
    dup = Node(1, "1")
    root.right = Node(2, "2", root)
    root.right.left = dup

    breakpoint()
    treevizer.to_png(root)
    # treevizer.dot_to_png()

    # print(bst[99])
    # print(41 in bst)
    # bst.remove(99)
    # bst.remove(41)
    # bst.inorder_traversal_print()
    # print(bst.get(99))
