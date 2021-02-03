"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import os
import re
import platform

POWERSHELL_PREFIX = "powershell.exe"
DOT_EXE = "dot.exe"
DOT = "dot"
CMD_STR = "{dot} -Tpng {dotfile} -o {pngfile}"

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
        dotfile = convert_cygwin_path_to_windows(dotfile)
        pngfile = convert_cygwin_path_to_windows(pngfile)

    cmd = CMD_STR.format(
        dot=dot,
        dotfile=dotfile,
        pngfile=pngfile,
    )
    return cmd



def convert_cygwin_path_to_windows(dir_path):
    """
    Solution from https://stackoverflow.com/a/50137718.
    Changed "\\" to "/", otherwise dot does not find files.
    """
    match = re.match('(/(cygdrive/)?)(.*)', dir_path)
    if not match:
        return dir_path.replace('/', '\\')
    dirs = match.group(3).split('/')
    dirs[0] = f'{dirs[0].upper()}:'
    return '/'.join(dirs)
