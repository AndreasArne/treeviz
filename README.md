# TreeViz
Repo for visualizing tree datasctructures in Python. Depend on Graphviz.

It builds dot files based on linked node objects. It creates the dot files and then calls Grapviz to turn them into pictures.



# Dependencies

This repo use [Graphviz](https://www.graphviz.org/) to create pictures from dot files. After installing Graphviz don't forget too add it to Path!



# Config

It is possible to change the Dot configuration to alter the resulting graph. To se available options look at [Graphviz's Dot documentaion](https://graphviz.org/doc/info/attrs.html). Put configuration in json format in `.dot.json` in your project folder.

Available parts to configure are the entire graph, vertexes/nodes and edges/arrows.

Example for changing color on arrows and nodes for the BalancedBinaryTreeGraph.

```
{
    "BalancedBinaryTreeGraph": {
        "node": {
            "fillcolor": "green",
        },
        "edge": {
            "color": "blue"
        }
    }
}
```


Development
------------------------

Run `make help` to see available commands.

### Cygwin

Integration tests don't work on cygwin. Images created on cygwin don't match with images created on Linux.



# To-Do
- [ ] Test on MacOS.
- [ ] Test on Linux.
- [ ] Add package to pip site so can pip install.
- [ ] Fix a properly readme.
- [X] Add support for linked lists.
- [X] Tox.
- [X] To not have .dot.json be mandatory.
- [X] Turn it into pip project.
- [X] Fix main.tree_to_dot(). It does not work.
- [X] Support cygwin.
- [X] Add red color to edges who couldn't be added and the Node it adds.
- [X] Remove depency on igraph. https://eli.thegreenplace.net/2009/11/23/visualizing-binary-trees-with-graphviz
- [X] Test on WSL.
- [X] Test on Cygwin - Can't install igraph. Not supported.
