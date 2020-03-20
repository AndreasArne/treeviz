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


    # def test_create_png(self):
    #     """
    #     For visual test of dot-to-png.
    #     """
    #     dir_path = path.dirname(path.realpath(__name__))
    #     expected_png = "tests/resources/tree.dot"
    #     expected_path = dir_path + "/" + expected_png
    #
    #     png.create_png(expected_png)

    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_wsl(self, platform_mock):
        """
        test the create_command function with wsl platform
        """
        platform_mock.platform.return_value = "Linux-4.4.0-17763-Microsoft-x86_64-with-Ubuntu-18.04-bionic"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/c/Users/Zeldah/git/treeviz"

        cmd = png.create_cmd(dotfile, pngfile, dir_path)
        self.assertEqual(
            cmd,
            "powershell.exe dot.exe -Tpng C:/Users/Zeldah/git/treeviz/tree.dot -o C:/Users/Zeldah/git/treeviz/tree.png"
        )



    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_mac(self, platform_mock):
        """
        test the create_command function with mac platform
        """
        platform_mock.platform.return_value = "Darwin-18.7.0-x86_64-i386-64bit"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/home/zeldah/git/treeviz"

        cmd = png.create_cmd(dotfile, pngfile, dir_path)
        self.assertEqual(cmd, "dot -Tpng /home/zeldah/git/treeviz/tree.dot -o /home/zeldah/git/treeviz/tree.png")



    @mock.patch("treeviz.exporters.png.platform")
    def test_create_cmd_linux(self, platform_mock):
        """
        test the create_command function with linux platform
        """
        platform_mock.platform.return_value = "Linux-4.19.84-standard-x86_64-with-debian-10.0"
        dotfile = "tree.dot"
        pngfile = "tree.png"
        dir_path = "/home/zeldah/git/treeviz"

        cmd = png.create_cmd(dotfile, pngfile, dir_path)
        self.assertEqual(cmd, "dot -Tpng /home/zeldah/git/treeviz/tree.dot -o /home/zeldah/git/treeviz/tree.png")



    @mock.patch("treeviz.exporters.png.wpc")
    def test_create_wsl_command_c_path(self, wpc_m):
        """
        test the create_wsl_command function with /c/ path for dir
        """
        expected_path = "C:/Users/Zeldah/git/treeviz"
        wpc_m.convert_m.return_value = expected_path
        dot_cmd = "powershell.exe dot.exe"

        windows_path_c = "/c/Users/Zeldah/git/treeviz"
        dot_and_dir = (dot_cmd, expected_path)
        self.assertEqual(dot_and_dir, png.create_wsl_command(windows_path_c))
        wpc_m.convert_m.assert_called_once_with(windows_path_c)



    @mock.patch("treeviz.exporters.png.wpc")
    def test_create_wsl_command_mnt_path(self, wpc_m):
        """
        test the create_wsl_command function with /mnt/ path for dir
        """
        expected_path = "C:/Users/Zeldah/git/treeviz"
        wpc_m.convert_m.return_value = expected_path
        dot_cmd = "powershell.exe dot.exe"

        windows_path = "/mnt/c/Users/Zeldah/git/treeviz"
        dot_and_dir = (dot_cmd, expected_path)
        self.assertEqual(dot_and_dir, png.create_wsl_command(windows_path))
        wpc_m.convert_m.assert_called_once_with(windows_path)



if __name__ == '__main__':
    unittest.main(verbosity=3)
