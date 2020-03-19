# TreeViz
Repo for visualizing tree datasctructures in Python. Use igraph and Graphviz



# Dependencies

This repo use [igraph](https://igraph.org/python/doc/tutorial/install.html#installing-igraph) to create dot files for tree structures and then [Graphviz](https://www.graphviz.org/) to create pictures from dot files. After installing Graphviz don't forget too add it to Path!

If you are using an older version of pip you can run into problems when installing igraph. Try updating pip, `pip3 install --upgrade pip`. You can use `make setup-venv` to create a venv and update its `pip` to the latest version. Then use `make install` to install Python requirements.

### Cygwin

Not supported! Can't install igraph on cygwin, dependency hell. Always something else that needs to be installed to be able to install igraph.



# To-Do
- [X] Test on WSL.
- [X] Test on Cygwin - Can't install igraph. Not supported.
- [ ] Test on MacOS.
- [ ] Test on Linux.
- [ ] Remove depency on igraph. https://eli.thegreenplace.net/2009/11/23/visualizing-binary-trees-with-graphviz


