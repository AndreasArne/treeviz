"""
Contain small helper functions for other modules to use.
"""

import os
import platform
import subprocess


def get_abspath(path):
    """
    Create absolute path for all OS.
    """
    path = os.path.abspath(path)
    info = platform.platform().lower()

    if "cygwin" in info:
        path = cyg_to_win_path(path)
    return path


def cyg_to_win_path(cyg_path):
    """
    Use "cygpath" on Cygwin to get windows type path which Graphviz can read.
    """
    return subprocess.check_output(["cygpath", "-w", cyg_path]).strip(b"\n").decode()
