from os import listdir
from os.path import isdir as is_dir

# Provisional 
only_dirs=False


def contents(top_path):
	"""
	inmmediate contents of top_path dir. 
	returns paths of subdirs, and file contents if the global only_dirs is false
	if none, or if path is a file, returns an empty list
	"""
    global only_dirs
    return [top_path+"/"+i for i in listdir(top_path)  if (is_dir(top_path+"/"+i) or not only_dirs)] if is_dir(top_path) else []

def deep_contents(top_path):
	'''
	Non-recursive way to get an unordered list of all the contents of top_path directory, at any level
	'''
	to_check=contents(top_path)
	checked=[]
	
	while len(to_check)>0:
		for path in to_check:
			to_check+=contents(path)
			to_check.remove(path)
			checked.append(path)
	
	return [top_path]+checked


			
			
			



			



			

