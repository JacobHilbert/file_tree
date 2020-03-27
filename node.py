from os import listdir
from os.path import isdir as is_dir

class Node:
	# this could be a directory or a file
	def __init__(self,path):
		self.path = path
		self.splitted = path.replace("./","").split("/")
		self.name = self.splitted[-1]
        self.level = len(self.splitted)-1
        self.is_last = False
		self.kind = "directory" if is_dir(self.path) else "file"
	def __repr__(self):
		return "<{}> {} at <{}>".format(self.name,self.kind,self.path[:-len(self.name)-1])
	def __str__(self):
		return "".join(self.splitted)
	
	
	
	
	
	
	
