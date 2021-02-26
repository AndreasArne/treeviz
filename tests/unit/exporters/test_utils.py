"""
Tests treevizer png exporter
"""
import unittest
from unittest import mock
from treevizer.exporters import utils

class TestUtils(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    @mock.patch("treevizer.exporters.utils.platform")
    @mock.patch("treevizer.exporters.utils.subprocess")
    def test_get_abspath_cygwin(self, subprocess_mock, platform_mock):
        """
        test the create_command function with cygwin platform
        """
        platform_mock.platform.return_value = "cygwin_nt-10.0-18363-3.1.7-340.x86_64-x86_64-64bit-windowspe"
        subprocess_mock.check_output.return_value = b'C:\\Users\\Zeldah\\git\\treevizer\\tree.png\n'

        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treevizer/"

        path = utils.get_abspath(dir_path+pngfile)
        self.assertEqual(
            path,
            'C:\\Users\\Zeldah\\git\\treevizer\\tree.png',
        )
        subprocess_mock.check_output.assert_called_once_with(
            ['cygpath', '-w', '/c/Users/Zeldah/git/treevizer/tree.png']
        )



    @mock.patch("treevizer.exporters.utils.platform")
    def test_get_abspath_wsl(self, platform_mock):
        """
        test the create_command function with wsl platform
        """
        platform_mock.platform.return_value = "Linux-4.4.0-17763-Microsoft-x86_64-with-Ubuntu-18.04-bionic"
        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treevizer/"

        path = utils.get_abspath(dir_path+pngfile)
        self.assertEqual(
            path,
            '/c/Users/Zeldah/git/treevizer/tree.png'
        )



    @mock.patch("treevizer.exporters.utils.platform")
    def test_get_abspath_mac(self, platform_mock):
        """
        test the create_command function with mac platform
        """
        platform_mock.platform.return_value = "Darwin-18.7.0-x86_64-i386-64bit"
        dotfile = "tree.dot"
        dir_path = "/home/zeldah/git/treevizer/"

        path = utils.get_abspath(dir_path+dotfile)
        self.assertEqual(
            path,
            '/home/zeldah/git/treevizer/tree.dot'
        )



    @mock.patch("treevizer.exporters.utils.platform")
    def test_get_abspath_linux(self, platform_mock):
        """
        test the create_command function with linux platform
        """
        platform_mock.platform.return_value = "Linux-4.19.84-standard-x86_64-with-debian-10.0"
        dotfile = "tree.dot"
        dir_path = "/home/zeldah/git/treevizer/"

        path = utils.get_abspath(dir_path+dotfile)
        self.assertEqual(
            path,
            '/home/zeldah/git/treevizer/tree.dot'
        )



if __name__ == '__main__':
    unittest.main(verbosity=3)
