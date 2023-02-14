"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import subprocess
from treevizer.exporters import utils

POWERSHELL_PREFIX = "powershell.exe"
DOT_EXE = "dot.exe"
DOT = "dot"
CMD_LIST = ["{dot_cmd}", "-Tpng", '"{dotfile}"', "-o", '"{pngfile}"']


def create_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Convert dot file to png using Graphviz
    """
    dotfile = utils.get_abspath(dotfile)
    pngfile = utils.get_abspath(pngfile)
    cmd = create_cmd(dotfile, pngfile)
    subprocess.run(cmd, check=True)


def create_cmd(dotfile, pngfile):
    """
    Create terminal command for creating png of dot file.
    """
    dot = DOT
    DOT_CMD_INDX = 0
    DOT_FILE_INDX = 2
    PNGF_FILE_INDX = 4
    cmd = CMD_LIST[:]
    cmd[DOT_CMD_INDX] = dot
    cmd[DOT_FILE_INDX] = f"{dotfile}"
    cmd[PNGF_FILE_INDX] = f"{pngfile}"
    return cmd
