"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import os
import re
import platform
import wsl_path_converter as wpc

def create_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Convert dot file to png using Graphviz
    """
    dir_path = os.path.dirname(os.path.realpath(__name__))
    cmd = create_cmd(dotfile, pngfile, dir_path)
    os.system(cmd)



def create_cmd(dotfile, pngfile, dir_path):
    """
    Create terminal command for creating png of dot file.
    """
    cmd_str = "{dot} -Tpng {dir}/{dotfile} -o {dir}/{pngfile}"
    dot = "dot"

    info = platform.platform().lower()
    if "microsoft" in info and "linux" in info:
        dot, dir_path = create_wsl_command(dir_path)
    elif "darwin" in info or "linux" in info:
        pass
    else:
        raise OSError("Your OS is not supported!")

    cmd = cmd_str.format(
        dot=dot,
        dir=dir_path,
        dotfile=dotfile,
        pngfile=pngfile,
    )
    return cmd



def create_wsl_command(dir_path):
    """
    Use wsl_path_converter to convert wsl format path to windows
    and return powershell command for graphviz/dot.
    """
    dot = "powershell.exe dot.exe"
    dir = wpc.convert_m(dir_path)
    return dot, dir
