from file_tree import Tree
from os import chdir
from graphviz import render

chdir("..")
chdir("..")
t=Tree("./file_tree")
chdir("./file_tree/examples")
t.export("tree.gv")
render("dot","png","tree.gv")
