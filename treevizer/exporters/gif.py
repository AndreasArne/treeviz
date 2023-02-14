"""
Turn structures to .GIF.
All images need to be the same size.
Too create "frames", make Vertexes and Edges invis and make them visible again
in order of apperance.
"""
import re
import glob
import copy
import tempfile
from treevizer.exporters import dot, png
from treevizer.exporters import utils

try:
    from PIL import Image
except ImportError:
    Image = None


def to_gif(graph, gif_path="recursion.gif", duration=800, loop=0):
    """
    Make helper module for for cygwin path
    """
    if Image is None:
        raise ImportError("Missing package Pillow. Install it to create GIFs.")

    gif_path = utils.get_abspath(gif_path)

    with tempfile.TemporaryDirectory(dir="./") as tmpdir:
        create_dot_frames(graph, tmpdir)
        create_images(tmpdir)
        create_gif(tmpdir, gif_path, duration, loop)


def natural_keys(text):
    """
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    """

    def atoi(text):
        return int(text) if text.isdigit() else text

    return [atoi(c) for c in re.split(r"(\d+)", text)]


def create_gif(tmpdir, gif_path, duration, loop):
    """
    use images to create gif
    """
    glob_pattern = f"{tmpdir}/*.png"
    imgs = [Image.open(f) for f in sorted(glob.glob(glob_pattern), key=natural_keys)]
    imgs[0].save(
        fp=gif_path,
        format="GIF",
        append_images=imgs[1:],
        save_all=True,
        duration=duration,
        loop=loop,
        optimize=True,
    )


def create_images(tmpdir):
    """
    create images of dot files
    """
    glob_pattern = f"{tmpdir}/*.dot"
    _ = [
        png.create_png(f, f.replace(".dot", ".png"))
        for f in sorted(glob.glob(glob_pattern))
    ]


def create_dot_frames(graph, tmp_path):
    """
    Create one frame for each vertex and edge. Copy edges and vertexes and set
    their styles to invis. Use style value to decide if it has already been added to a frame
    or if it should get own fram.

    Use order of edges in list as controll for order to vertexes were added to the graph.

    We don't care if frame_counter value is not same as number of frames,
    we only use it to create unique filenames with order.
    """
    frame_counter = 0
    # Save copy of vertexes and edges, as reference for original values
    vertexes = copy.deepcopy(graph.vertexes)
    edges = copy.deepcopy(graph.edges)

    # Set style to invis on everything in graph
    for vertex in graph.vertexes.values():
        vertex.options["style"] = "invis"
    for edge in graph.edges:
        edge.options["style"] = "invis"

    # restore style on current frame and output dot code for frames
    for index, edge in enumerate(edges):
        write_dot_frame(
            graph.vertexes[edge.src],
            vertexes[edge.src],
            f"{tmp_path}/frame{frame_counter}.dot",
            graph,
        )
        frame_counter += 1

        write_dot_frame(
            graph.edges[index], edge, f"{tmp_path}/frame{frame_counter}.dot", graph
        )
        frame_counter += 1

        write_dot_frame(
            graph.vertexes[edge.dest],
            vertexes[edge.dest],
            f"{tmp_path}/frame{frame_counter}.dot",
            graph,
        )
        frame_counter += 1


def write_dot_frame(graph_element, copy_element, path, graph):
    """
    If original style is not invis and style in graph is not already updated
    to original value, create frame.
    """
    if (
        graph_element.options["style"] == "invis"
        and copy_element.options.get("style", "") != "invis"
    ):
        graph_element.options["style"] = copy_element.options.get("style", "")
        dot.to_dot(graph, path)
