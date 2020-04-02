from .tree import *
from sys import argv


def main(default,top_path=".",*args):
    only_dirs = "-d" in args
    include_hidden = "-a" in args
    tree = Tree(top_path,only_dirs)
    tree.make_tree(include_hidden)

if __name__ == "__main__":
    main(*argv)
