"""
Tests treevizer png exporter
"""
import unittest
from unittest import mock
from treevizer.exporters import png

class TestPngExporter(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    @mock.patch("treevizer.exporters.png.subprocess")
    @mock.patch("treevizer.exporters.png.utils")
    def test_create_cmd_cygwin(self, utils_mock, subprocess_mock):
        """
        test the create_command function with wsl platform
        """
        utils_mock.get_abspath.side_effect = [
            'C:\\Users\\Zeldah\\git\\treevizer\\tree.dot',
            'C:\\Users\\Zeldah\\git\\treevizer\\tree.png',
        ]
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treevizer/"

        png.create_png(dir_path+dotfile, dir_path+pngfile)

        subprocess_mock.run.assert_called_once_with(
            ['dot', '-Tpng', 'C:\\Users\\Zeldah\\git\\treevizer\\tree.dot', '-o', 'C:\\Users\\Zeldah\\git\\treevizer\\tree.png'],
            check=True
        )



if __name__ == '__main__':
    unittest.main(verbosity=3)
