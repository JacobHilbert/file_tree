from .tree import Tree
from sys import argv

def main(default,top_path=".",*args):
	include_fies = "-d" not in args
	include_hidden = "-h" in args
	print(Tree(top_path,include_fies,include_hidden))

if __name__ == "__main__":
	main(*argv)
