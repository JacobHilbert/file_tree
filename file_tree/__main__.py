from .tree import Tree
from sys import argv

def main(default,top_path=".",*args):
	include_files = "-d" not in args
	include_hidden = "-h" in args
	export_dot = "-dot" in args
	export_txt = "-txt" in args

	if not (export_dot or export_txt):
		print(Tree(top_path,include_files,include_hidden))
	elif export_dot:
		Tree(top_path,include_files,include_hidden).export("tree.gv")
	elif export_txt:
		Tree(top_path,include_files,include_hidden).export("tree.txt")

if __name__ == "__main__":
	main(*argv)
