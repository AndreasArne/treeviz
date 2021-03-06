"""
Tests Treeviz png exporter
"""
import unittest
import filecmp
import shutil
from unittest import mock
from pathlib import Path
from os import path
#pylint: disable=no-name-in-module,import-error, protected-access, attribute-defined-outside-init
from treeviz.exporters import png

class TestPngExporter(unittest.TestCase):
    """Submodule for unittests, derives from unittest.TestCase"""

    def test_convert_cygwin_path_to_windows(self):
        """
        Asser that cygrive path are converted correctly
        """
        dir_path = "/cygdrive/c/Users/Zeldah/git/treeviz"
        path = png.convert_cygwin_path_to_windows(dir_path)
        self.assertEqual(path, "C:/Users/Zeldah/git/treeviz")



    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_cygwin(self, platform_mock):
        """
        test the create_command function with wsl platform
        """
        platform_mock.platform.return_value = "cygwin_nt-10.0-18363-3.1.7-340.x86_64-x86_64-64bit-windowspe"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treeviz/"

        cmd = png.create_cmd(dir_path+dotfile, dir_path+pngfile)
        self.assertEqual(
            cmd,
            "dot -Tpng C:/Users/Zeldah/git/treeviz/tree.dot -o C:/Users/Zeldah/git/treeviz/tree.png"
        )



    @mock.patch("treeviz.exporters.png.wpc")
    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_wsl(self, platform_mock, wpc_mock):
        """
        test the create_command function with wsl platform
        """
        platform_mock.platform.return_value = "Linux-4.4.0-17763-Microsoft-x86_64-with-Ubuntu-18.04-bionic"
        wpc_mock.convert_m.return_value = "C:/Users/Zeldah/git/treeviz"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treeviz/"

        cmd = png.create_cmd(dir_path+dotfile, dir_path+pngfile)
        self.assertEqual(
            cmd,
            "dot -Tpng /c/Users/Zeldah/git/treeviz/tree.dot -o /c/Users/Zeldah/git/treeviz/tree.png"
        )



    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_mac(self, platform_mock):
        """
        test the create_command function with mac platform
        """
        platform_mock.platform.return_value = "Darwin-18.7.0-x86_64-i386-64bit"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/home/zeldah/git/treeviz/"

        cmd = png.create_cmd(dir_path+dotfile, dir_path+pngfile)
        self.assertEqual(cmd, "dot -Tpng /home/zeldah/git/treeviz/tree.dot -o /home/zeldah/git/treeviz/tree.png")



    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_linux(self, platform_mock):
        """
        test the create_command function with linux platform
        """
        platform_mock.platform.return_value = "Linux-4.19.84-standard-x86_64-with-debian-10.0"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/home/zeldah/git/treeviz/"

        cmd = png.create_cmd(dir_path+dotfile, dir_path+pngfile)
        self.assertEqual(cmd, "dot -Tpng /home/zeldah/git/treeviz/tree.dot -o /home/zeldah/git/treeviz/tree.png")

if __name__ == '__main__':
    unittest.main(verbosity=3)
