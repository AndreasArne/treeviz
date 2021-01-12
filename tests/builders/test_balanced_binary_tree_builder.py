"""
Tests Treeviz builders
"""
import unittest
from unittest import mock
from fixtures import tree_utils as utils
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from fixtures.bst import BinarySearchTree as Bst
from fixtures.bst import Node
from treeviz.builders.balanced_binary_tree import BalancedBinaryTreeGraph as BbtBuilder
from treeviz.exporters import png, dot

class TestBuilders(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def _setUp(self, size):
        """ Custom setup to control size of tree use for tests """
        self.bst = Bst()
        self.insert_seq = utils.random_seq(size)
        utils.list_to_bst(self.insert_seq, self.bst)

    def tearDown(self):
        """ teardown test """
        self.bst = None
        self.insert_seq = None



    # def test_bbt_to_png(self):
    #     """
    #     Method for creating a picture of tree,
    #     Nothing is tested. 
    #     """
    #     nr_tree_nodes = 11
    #     self._setUp(nr_tree_nodes)
    #     # Adds a ghost node
    #     self.bst.root.left.parent = Node(99,99)
    # 
    #     bbt = BbtBuilder(self.bst.root)
    #     dot.to_dot(bbt)
    #     png.create_png()



    # def test_create_bbt_sucessfully(self):
    #     """
    #     Try create a balance binary tree
    #     from a binary search tree.
    #     Bad test, too big! But works wonderfully
    #     """
    #     nr_tree_nodes = 11
    #     self._setUp(nr_tree_nodes)
    #     # lägg till en ghost node och kolla att den får röd färg
    #     # self.bst.root.left.parent = Node(99,99)
    #     bbt = BbtBuilder(self.bst.root)
    #     NR_CHILD_NODES_P_NODE = 3
    #     graph_number_nodes = nr_tree_nodes * NR_CHILD_NODES_P_NODE + 1 # 1 for root node
    # 
    #     # uncomment to se files
    # 
    #     # dot.to_dot(bbt)
    #     # png.create_png()
    #     # exit()
    # 
    #     # Check correct number of nodes in tree
    #     self.assertEqual(len(bbt.vertexes), graph_number_nodes)
    # 
    #     # Check correct visible nodes
    #     graph_nodes = bbt.vertexes
    #     # print(graph_nodes)
    #     for i in range(nr_tree_nodes):
    #         vertex = graph_nodes[str(i)]
    #         self.assertEqual(vertex.options["name"], str(i))
    #         self.assertEqual(vertex.name, str(i))
    #         self.assertEqual(vertex.options["style"], "filled")
    # 
    #     # Check correct invis nodes to balance tree
    #     nr_invis_nodes = graph_number_nodes - nr_tree_nodes
    #     for i in range(1, nr_invis_nodes):
    #         vertex = graph_nodes["i" + str(i)]
    #         self.assertEqual(vertex.options["name"], "i" + str(i))
    #         self.assertEqual(vertex.name, "i" + str(i))
    #         self.assertEqual(vertex.options["style"], "invis")
    # 
    #     one_less_reference_for_root = 0
    #     print(bbt.edges)
    #     for node in utils.get_nodes_neighbors(self.bst.root):
    #         if node[1] is not None:
    #             bbt.edges.index((node[0], node[1]))
    #         if node[2] is not None:
    #             bbt.edges.index((node[0], node[2]))
    #         if node[3] is not None:
    #             bbt.edges.index((node[0], node[3]))
    # 
    #         # print(edges)
    #         # check arrows to node
    #         in_nodes = [n["name"] for n in bbt.graph.vs.find(name=node[0]).predecessors()]
    #         node_references = node[1:]
    #         for n in in_nodes:
    #             if not n.startswith("i"):
    #                 self.assertIn(n, node_references)
    # 
    #         # check arrows from node
    #         out_nodes = [n["name"] for n in bbt.graph.vs.find(name=node[0]).successors()]
    #         expected_nr_invis_nodes = one_less_reference_for_root + node_references.count(None)
    #         invis_node_counter = 0
    #         for n in out_nodes:
    #             if n.startswith("i"):
    #                 invis_node_counter += 1
    #             else:
    #                 self.assertIn(n, node_references)
    #         self.assertEqual(expected_nr_invis_nodes, invis_node_counter)
    #         one_less_reference_for_root = 1



    def test_create_bbt_on_empty_tree(self):
        """
        Try create a balance binary tree with None sent as root
        """
        with self.assertRaises(ValueError):
            _ = BbtBuilder(None)



    def test_add_vertex_no_kwargs(self):
        """
        add vertex correctly, no kwargs
        """
        root = Node(1, 1)

        bbt = BbtBuilder(root)
        with mock.patch('treeviz.builders.balanced_binary_tree.Vertex') as vertexMock:
            bbt._add_vertex(2)

            vertexMock.assert_called_once_with(2)
            
        self.assertEqual(len(bbt.vertexes), 5) # 5 with invis nodes



    def test_add_vertex_kwargs(self):
        """
        add vertex correctly with kwargs
        """
        root = Node(1, 1)

        bbt = BbtBuilder(root)
        with mock.patch('treeviz.builders.balanced_binary_tree.Vertex') as vertexMock:
            bbt._add_vertex(2, style="filled", color="red")

            vertexMock.assert_called_once_with(2, style="filled", color="red")
            
        self.assertEqual(len(bbt.vertexes), 5) # 5 with invis nodes



    def test_add_vertex_already_exist(self):
        """
        Testa that error is raised when a Vertex already exist.
        """
        root = Node(1, 1)
        
        bbt = BbtBuilder(root)
        with self.assertRaises(KeyError):
            bbt._add_vertex(1)



    def test_add_edge_raise_exception_when_src_vertex_missing(self):
        """
        add edge when the source vertex is missing
        """
        root = Node(1, 1)

        bbt = BbtBuilder(root)
        with self.assertRaises(ValueError):
            bbt._add_edge(2, 1, "not relevant")



    def test_add_edge(self,):
        """
        add edge when all vertexes exist.
        """
        src_id = 0
        dest_id = 1

        with mock.patch.object(BbtBuilder, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            bbt = BbtBuilder("")
            src_mock = mock.MagicMock()
            src_mock.id = src_id
            dest_mock = mock.MagicMock()
            dest_mock.id = dest_id
            bbt.vertexes[1] = src_mock
            bbt.vertexes[2] = dest_mock

            with mock.patch('treeviz.builders.balanced_binary_tree.Edge') as edgeMock:
                bbt._add_edge(1, 2, "parent")

                edgeMock.assert_called_once_with(src_id, dest_id)

        self.assertEqual(len(bbt.vertexes), 2)
        self.assertEqual(len(bbt.edges), 1)



    @mock.patch('builtins.print')
    def test_add_edge_when_dest_vertex_missing(self, mock_print):
        """
        add edge when the destination vertex is missing.
        """
        src_id = 0
        dest_id = 1
        def side_effect(self_, name, label, color):
            self.assertEqual(color, "red")
            self.assertEqual(name, 2)
            self.assertEqual(label, 2)

            dest_mock = mock.MagicMock()
            dest_mock.id = dest_id
            self_.vertexes[2] = dest_mock

        with mock.patch.object(BbtBuilder, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            bbt = BbtBuilder("")
            src_mock = mock.MagicMock()
            src_mock.id = src_id
            bbt.vertexes[1] = src_mock
            
            with mock.patch.object(BbtBuilder, '_add_vertex', autospec=True, side_effect=side_effect):
                with mock.patch('treeviz.builders.balanced_binary_tree.Edge') as edgeMock:
                    bbt._add_edge(1, 2, "parent")

                    edgeMock.assert_called_once_with(src_id, dest_id, label="parent", color="red")

        mock_print.assert_called_once()
        self.assertEqual(len(bbt.vertexes), 2)
        self.assertEqual(len(bbt.edges), 1)



    def test_add_invis_node_mock(self):
        """
        add an invis node
        """
        inv_key = "i1"
        inv_id = 1
        src_id = 0
        src_key = "1"
        src_mock = mock.MagicMock()
        src_mock.id = src_id

        def add_vertex(self_, name, label, style):
            self.assertEqual(name, inv_key)
            self.assertEqual(label, inv_key)
            self.assertEqual(style, "invis")

            inv_vertex_mock = mock.MagicMock()
            inv_vertex_mock.id = inv_id
            self_.vertexes[inv_key] = inv_vertex_mock

        with mock.patch.object(BbtBuilder, "_add_node_to_graph", lambda x, y: None): # Match number of args for init and return None
            with mock.patch.object(BbtBuilder, '_add_vertex', autospec=True, side_effect=add_vertex):
                with mock.patch('treeviz.builders.balanced_binary_tree.Edge') as edgeMock:
                    bbt = BbtBuilder("")
                    bbt.vertexes[src_key] = src_mock
                    bbt._add_invis_node(src_key)
    
            self.assertEqual(bbt.invis_counter, 1)
            edgeMock.assert_called_once_with(src_id, inv_id, style="invis", weight=5)
            self.assertEqual(len(bbt.edges), 1)
            self.assertEqual(len(bbt.vertexes), 2)



if __name__ == '__main__':
    unittest.main(verbosity=3)
