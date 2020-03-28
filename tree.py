from .contents import *
from .node import *

class Tree:

	def __init__(self,top_path,only_dirs=True):
		self.only_dirs=only_dirs
		self.path_list = list(sorted(deep_contents(top_path,only_dirs)))
		self.node_list = [ Node(i) for i in self.path_list ]
		self.node_dict = {}

	def fill_dict(self):
		for i,j in zip(self.path_list,self.node_list):
			self.node_dict[i]=j

	def register_nodes_children(self):
		# register children
		for node in self.node_list:
			node.children += [ self.node_dict[i] for i in sorted(contents(node.path,self.only_dirs)) ]

	def format_node(self,current_node):
		other_nodes = [ other for other in self.node_list if other != current_node ]

		# run through all the other nodes
		for other in other_nodes:
			try:
				if current_node.path in other.path:
					if current_node.children[-1].path not in other.path:
						other.splitted[current_node.level] = "│"+(" "*3)
					else:
						other.splitted[current_node.level] = " "*4
			except IndexError:
				pass
		# run through the current_node's children
		for child in current_node.children:
			child.splitted[current_node.level] = "├"+(2*"─")+" "
		# fix last children
		try:
			current_node.children[-1].splitted[current_node.level] = "└"+(2*"─")+" "
		except IndexError: #because can have no children, so children[-1] will send this to hell
			pass

	def make_tree(self):
		self.fill_dict()
		self.register_nodes_children()
		for node in self.node_list:
			self.format_node(node)
		for node in self.node_list:
			print(node)
