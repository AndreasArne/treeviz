"""
Configuration for dot graphs.

Merges config from files with config from code.
https://stackoverflow.com/a/26853961
So there is configuration available even if user does not have config file (.dot.json).
And users can ovveride configurations locally.
"""
import json
from pathlib import Path
from collections.abc import MutableMapping


DEFAULT_DOT_CONFIGS = {
    "LinkedListGraph": {
        "graph": {
            "rankdir": "LR"
        },
        "node": {
            "style": "filled",
            "fillcolor": "lightblue",
            "shape": "circle",
            "fixedsize": "true",
            "width": 1
        },
        "edge": {
            "arrowsize": 1,
            "color": "black"
        }
    },
    "BalancedBinaryTreeGraph": {
        "graph": {
            "nodesep": 0.25,
            "ranksep": 0.3,
            "splines": "line"
        },
        "node": {
            "style": "filled",
            "fillcolor": "lightblue",
            "shape": "circle",
            "fixedsize": "true",
            "width": 0.5
        },
        "edge": {
            "arrowsize": 0.8,
            "color": "black"
        }
    }
}

CONFIG_FILENAME = ".dot.json"



def get_config(graph_type):
    """
    If config file exist merge, otherwise use hardcoded config.
    """

    file_config = read_config(graph_type)
    if file_config is not None:
        merged_config = merge_configs(
            DEFAULT_DOT_CONFIGS[graph_type],
            file_config
        )
        return merged_config

    return DEFAULT_DOT_CONFIGS[graph_type]



def read_config(graph_type):
    """
    Read config from file.
    """
    config_file = Path(CONFIG_FILENAME)
    if config_file.is_file():
        with open(CONFIG_FILENAME) as fd:
            config_json = json.load(fd)
        return config_json.get(graph_type, None)
    return None


def merge_configs(d1, d2):
    '''
    Update two dicts of dicts recursively,
    if either mapping has leaves that are non-dicts,
    the second's leaf overwrites the first's.
    https://stackoverflow.com/a/24088493
    '''
    for k, v in d1.items():
        if k in d2:
            # if both values from d1 and d2 are of instance MutableMapping
            if all(isinstance(e, MutableMapping) for e in (v, d2[k])):
                d2[k] = merge_configs(v, d2[k])
            # we could further check types and merge as appropriate here.
    d3 = d1.copy()
    d3.update(d2)
    return d3
