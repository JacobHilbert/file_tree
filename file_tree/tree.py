from .utils import deep_contents,contents
from .node import Node

class Tree:

	def __init__(self,top_path=".",include_files=True,include_hidden=False):
		self.include_files = include_files
		self.include_hidden= include_hidden
		self.root = top_path
		self.nodes = [Node(i) for i in deep_contents(top_path,include_files,include_hidden)]
		self.nodes.sort()
		self.node_dict = {_path:_node for _path,_node in zip( [node.path for node in self.nodes] ,self.nodes)}

		for node in self.nodes:
			self.register_children(node)

		for node in self.nodes:
			self.format_node(node)

	def __repr__(self):
		return "Tree(top_path=\"{}\",include_files={},include_hidden={})".format(self.root,self.include_files,self.include_hidden)

	def __str__(self):
		return "".join([str(node)+"\n" for node in self.nodes])


	def register_children(self,node):
		node.children += [self.node_dict[i] for i in contents(node.path,self.include_files,self.include_hidden)]
		node.children.sort()

	def format_node(self,current_node):
		other_nodes = [ other for other in self.nodes if other != current_node ]

		# run through all other nodes
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
		except IndexError: # because current_node can have no children, so children[-1] will send this to hell
			pass

	def kind_count(self):
		dirs = [ node for node in self.nodes if node.kind == "directory" ]
		files = [ node for node in self.nodes if node.kind == "file" ]
		hidden_dirs = [ node for node in dirs if node.is_hidden ]
		hidden_files = [ node for node in files if node.is_hidden ]
		return \
		f"{len(dirs)} directories" + \
		f" ({len(hidden_dirs)} hidden)"*(self.include_hidden) + \
		"." + \
		f"\n{len(files)} files"*(self.include_files) + \
		f" ({len(hidden_files)} hidden)"*(self.include_files*self.include_hidden) + \
		"."*(self.include_files)
