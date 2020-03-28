from .tree import *
from sys import argv


def main(default,top_path,only_dirs):
    print(only_dirs)
    tree = Tree(top_path,only_dirs==True)
    tree.make_tree()

if __name__ == "__main__":
    main(*argv)
