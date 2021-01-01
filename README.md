# TreeViz
Repo for visualizing tree datasctructures in Python. Depend on Graphviz.

It builds dot files based on linked node objects. It creates the dot files and then calls Grapviz to turn them into pictures.



# Dependencies

This repo use [Graphviz](https://www.graphviz.org/) to create pictures from dot files. After installing Graphviz don't forget too add it to Path!



# To-Do
- [ ] Fix main.tree_to_dot(). It does not work.
- [ ] Test on MacOS.
- [ ] Test on Linux.
- [ ] Turn it into pip project.
- [ ] Add support for linked lists.
- [ ] Tox.
- [X] Support cygwin.
- [X] Add red color to edges who couldn't be added and the Node it adds.
- [X] Remove depency on igraph. https://eli.thegreenplace.net/2009/11/23/visualizing-binary-trees-with-graphviz
- [X] Test on WSL.
- [X] Test on Cygwin - Can't install igraph. Not supported.
