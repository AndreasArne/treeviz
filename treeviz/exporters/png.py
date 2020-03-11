"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import os
import re
import platform

def create_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Use powershell to convert dot file to png using Graphviz
    """
    dir_path = os.path.dirname(os.path.realpath(__name__))
    cmd = create_cmd(dotfile, pngfile, dir_path)
    print(cmd)
    os.system(cmd)



def create_cmd(dotfile, pngfile, dir_path):
    info = platform.platform().lower()
    cmd = "{dot} -Tpng {dir}/{dotfile} -o {dir}/{pngfile}"

    if "microsoft" in info and "linux" in info:
        cmd = create_wsl_command(cmd, dir_path)
    elif "cygwin" in info:
        # cant install igraph on cygwin
        pass
    elif "darwin" in info or "linux" in info:
        cmd = cmd.format(
            dot="dot",
            dir=dir_path,
            dotfile=dotfile,
            pngfile=pngfile,
        )
    else:
        raise OSError("Your OS is not supported!")
    return cmd



def create_wsl_command(cmd, dir_path):
    cmd.format(
        dot="dot.exe",
        dir=fix_c_in_windows_path(dir_path),
    )
    cmd = "powershell.exe 'dot.exe " + cmd + ";exit"
    return cmd

def fix_c_in_windows_path(path):
    """
    Fix wsl path in windows to work in powershell.
    """
    if path.startswith("/c/"):
        path = path.replace("/c/", "C:/")
    return path
