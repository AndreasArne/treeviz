"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import os
import subprocess
import platform

POWERSHELL_PREFIX = "powershell.exe"
DOT_EXE = "dot.exe"
DOT = "dot"
CMD_STR = '{dot} -Tpng "{dotfile}" -o "{pngfile}"'

def create_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Convert dot file to png using Graphviz
    """
    dotfile = os.path.abspath(dotfile)
    pngfile = os.path.abspath(pngfile)
    cmd = create_cmd(dotfile, pngfile)
    os.system(cmd)



def create_cmd(dotfile, pngfile):
    """
    Create terminal command for creating png of dot file.
    """
    dot = DOT
    info = platform.platform().lower()
    if "cygwin" in info:
        dotfile = cyg_to_win_path(dotfile)
        pngfile = cyg_to_win_path(pngfile)

    cmd = CMD_STR.format(
        dot=dot,
        dotfile=dotfile,
        pngfile=pngfile,
    )
    return cmd

def cyg_to_win_path(cyg_path):
    """
    Use "cygpath" on Cygwin to get windows type path which Graphviz can read.
    """
    return subprocess.check_output(["cygpath", "-w", cyg_path]).strip(b"\n").decode()
