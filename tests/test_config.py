"""
Test config reader
"""
import unittest
from unittest import mock
from treeviz import config

class TestConfig(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""



    @mock.patch("treeviz.config.read_config")
    def test_get_config_missing_graphtype(self, mock_read):
        """
        Test that KeyError is raised when graph type is missing in default configs.
        """
        mock_read.return_value = {"y": 1}
        with self.assertRaises(KeyError):
            config.get_config("missing")



    @mock.patch("treeviz.config.read_config")
    def test_get_config_merge_with_file(self, mock_read):
        """
        Test that config file gets merged with default if file exist.
        """
        mock_read.return_value = {"y": 1}
        graph_type = "x"
        with mock.patch("treeviz.config.DEFAULT_DOT_CONFIGS", {"x": {"y": 2}}) as _:
            self.assertEqual(
                config.get_config(graph_type),
                {"y": 1}
            )



    def test_get_config_read_json_none(self):
        """
        Test that default config is returned when read_config returns None.
        """
        with mock.patch('treeviz.config.read_config') as read_mock:
            read_mock.return_value = None
        
            self.assertEqual(
                config.get_config("BalancedBinaryTreeGraph"),
                config.DEFAULT_DOT_CONFIGS["BalancedBinaryTreeGraph"]
            )



    @mock.patch("treeviz.config.json")
    @mock.patch("treeviz.config.Path")
    def test_read_config(self, mock_path, mock_json):
        """
        Test that a graphs config i return from file if exist
        """
        mock_path.is_file.return_value = True
        mock_json.load.return_value = {"graph": 1}
        self.assertEqual(config.read_config("graph"), 1)



    def test_read_config_missing_file(self):
        """
        Test that None is returned if there is no config file to read
        """
        self.assertIsNone(config.read_config(""))



    @mock.patch("treeviz.config.json")
    @mock.patch("treeviz.config.Path")
    def test_read_config_with_missing_graph_type(self, mock_path, mock_json):
        mock_path.is_file.return_value = True
        mock_json.load.return_value = {}
        self.assertIsNone(
            config.read_config("missing"),
        )



    def test_merge_config(self):
        """
        Test mergin of two dictionaries
        """
        d1 = {
            "x": 1,
            "y": {
                "y.x": [1, 2, 3],
                "y.y": {
                    "y.y.y": "test",
                    "y.y.z": 2
                }
            },
            "w": 3
        }
        d2 = {
            "z": 2,
            "w": 4,
            "y": {
                "y.y": {
                    "y.y.x": 1,
                    "y.y.y": 3
                }
            }
        }
        self.assertEqual(
            config.merge_configs(d1, d2),
            {
                'w': 4,
                'x': 1,
                'y': 
                {
                    'y.x': [1, 2, 3],
                    'y.y': {
                        'y.y.x': 1,
                        'y.y.y': 3,
                        'y.y.z': 2
                    }
                },
                'z': 2
            }
        )
