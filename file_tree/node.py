from os import listdir
from os.path import isdir as is_dir

class Node:
	# this could be a directory or a file
	def __init__(self,path):
		self.path = path
		self.splitted = path[1:].split("/")
		self.name = self.splitted[-1]
		self.level = len(self.splitted)-1
		self.is_last = False
		self.is_hidden = self.name.startswith(".")
		self.kind = "directory" if is_dir(self.path) else "file"
		self.children = []

	def __repr__(self):
		return f"Node({self.path})"

	def __str__(self):
		return "".join(self.splitted) if self.path!="." else "."

	def value(self):
		# this works!
		parts=self.path.split("/")
		return ("".join(sum([ ["directory_",i,"/"] for i in parts[:-1] ],[])+[self.kind,"_",self.name])).replace(".","")

	def __lt__(self,other):
		return self.value() < other.value()
