# Treevizer

Visualize node data structures using [Graphviz](https://graphviz.org/).



## How it works

Treevizer iterates over your datastructure to generate a DOT file and runs Graphviz turn it into an image. The datastructure needs to be built using Nodes.

It also support recursive functions.

### Examples

#### Linked list

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/ll.png" alt="Image of linked list">
</p>

#### Balanced binary tree

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/bst.png" alt="Image of Balanced binary tree">
</p>

#### Trie

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/trie.png" alt="Image of Trie">
</p>

#### Recursive Fibonacci

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/fibonacci.gif" alt="Image of recursive Fibonacci function">
</p>

### Prerequisites

You need to install [Graphviz](https://graphviz.org/download/) and make sure it is in $PATH.

#### Cygwin

Graphviz and Pillow need special installation on Cygwin.

##### Graphviz

Don't install Graphviz in Cygwin, do a windows installation. Otherwise there will be a problem with paths.

##### Pillow

Don't install Pillow with pip, instead do it with a Cygwin package. Install the Cygwin package `python3X-imagin`, replace `X` with your Python version.

Pillow is used to create GIFs.



### Installing

```
pip install treevizer
```



## Usage

The following structures are supported:

### Linked list (ll)

Structure type is called "ll". The config key is called "LinkedList".

Require a Node class with the attributes that fulfill the following class diagram.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/ll_node_cls.png" alt="Class diagram of Node class for linked list.">
</p>



### Balanced binary tree (bbt)

Structure type is called "bbt". The config key is called "BalancedBinaryTree".

Require a Node class with the attributes that fulfill the following class diagram.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/bst_node_cls.png" alt="Class diagram of Node class for Balance binary tree.">
</p>



### Trie (trie)

Structure type is called "trie". The config key is called "Trie".

Require a Node class with the attributes that fulfill the following class diagram.

<p align="center">
  <img src="https://raw.githubusercontent.com/AndreasArne/treeviz/master/img/trie_node_cls.png" alt="Class diagram of Node class for Trie.">
</p>

The `stop` attribute marks if node marks a word (True) or not (False).



### Recursion

Decorate your recursive function with `recursion_viz`. It is possible to decorate multiple functions. Each function is identified by the name of your function when creating the PNG or GIF.

#### Example
```python
import treevizer

@treevizer.recursion_viz
def a_rec_func():
    a_rec_func()


@treevizer.recursion_viz
def another_rec_func():
    another_rec_func()

a_rec_func()
another_rec_func()

treevizer.recursion_to_png("a_rec_func", dot_path="recursion.dot", png_path="recursion.png")
treevizer.recursion_to_png("another_rec_func", dot_path="rec2.dot", png_path="rec2.png")
```

To configure the dot language, use "Recursion" as key in the json.



### Functions

#### Structure to DOT file

```python
import treevizer

treevizer.to_dot(root, structure_type="bbt", dot_path="tree.dot")
    """
    Generate DOT file from node structure.

    Parameters
    ----------
    root : Node
        Root node for datastructure
    structure_type : str
        Name of the type of datastructure (default is "bbt")
    dot_path : str
        Path to generated DOT file (default is tree.dot)
    """
```



#### Structure to PNG

This also creates a DOT file.

```python
import treevizer

treevizer.to_png(root, structure_type="bbt", dot_path="tree.dot", png_path="tree.png")
    """
    Generate DOT file from node structure and use Graphviz to create image.

    Parameters
    ----------
    root : Node
        Root node for datastructure
    structure_type : str
        Name of the type of datastructure (default is "bbt")
    dot_path : str
        Path to generated DOT file (default is tree.dot)
    png_path : str
        Path to generated png file (default is tree.png)
    """
```



#### Recursion to PNG

This also creates a DOT file.

```python
import treevizer

@treevizer.recursion_viz
def a_recusive_function():
    a_recusive_function()


treevizer.recursion_to_png(function_name, dot_path="recursion.dot", png_path="recursion.png")
    """
    Generate DOT file of recursive function calls and use Graphviz to create image.

    Parameters
    ----------
    function_name : str
        Name of your decorated function.
    dot_path : str
        Path to generated DOT file (default is recursion.dot)
    png_path : str
        Path to generated png file (default is recursion.png)
    """
```



#### Recursion to GIF

```python
import treevizer

@treevizer.recursion_viz
def a_recusive_function():
    a_recusive_function()


treevizer.recursion_to_gif(function_name, gif_path="recursion.dot", duration=800, loop=0)
    """
    Generate PNG files of recursive function calls and use Pillow to create GIF.

    Parameters
    ----------
    function_name : str
        Name of your decorated function.
    gif_path : str
        Path to generated GIF file (default is recursion.gif)
    duration : int
        duration, in miliseconds, of how long each image will be displayed in the GIF (default is 800)
    loop : int
        how many times the GIF should loop after initial loop. 0 to loop infinitely (default is 0)
    """
```



#### DOT file to PNG

```python
import treevizer

treevizer.dot_to_png(dot_path="tree.dot", png_path="tree.png")
    """
    Use Graphviz to create image from a DOT file.

    Parameters
    ----------
    dot_path : str
        Path to your DOT file (default is tree.dot)
    png_path : str
        Path to generated png file (default is tree.png)
    """
```


### Configure

Create `.dot.json` in root folder to change DOT configuration.  Available options can be found in [Graphviz documentation](https://graphviz.org/doc/info/attrs.html).

For example to change color of Nodes in image for balanced binary tree use the following.

```
# .dot.json
{
    "BalancedBinaryTree": {
        "node": {
            "fillcolor": "green"
        }
    }
}
```

To change size and shape of nodes and color of edges in Linked list use the following.

```
# .dot.json
{
    "LinkedList": {
        "node": {
            "shape": "square",
            "width": 1.5
        },
        "edge": {
            "color": "red"
        }
    }
}
```

To change color of the font on edge labels for recursion.

```
{
    "Recursion": {
        "edge": {
            "fontcolor": "black"
        }
    }
}
```

## Known Errors/Warnings

[Known Errors and Warnings](https://github.com/AndreasArne/treeviz/issues/1)



## Links

- [Pypi](https://pypi.org/project/treevizer/)
- [Source code](https://github.com/AndreasArne/treeviz)



## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
