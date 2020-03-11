"""
Export dot file to png using Graphviz
Needs to have Graphviz installed and in path.
"""
import os
import re

def create_png(dotfile="tree.dot", pngfile="tree.png"):
    """
    Use powershell to convert dot file to png using Graphviz
    """
    folder_path = fix_c_in_windows_path(os.path.dirname(os.path.realpath(__name__)))
    dot_cmd = "dot.exe -Tpng {} -o {}".format(dotfile, pngfile)
    cmd = "powershell.exe 'cd {path}; {cmd};exit'".format(path=folder_path, cmd=dot_cmd)
    print(cmd)
    os.system(cmd)



def fix_c_in_windows_path(path):
    """
    Fix wsl path in windows to work in powershell.
    """
    if path.startswith("/c/"):
        path = path.replace("/c/", "C:/")
    return path
