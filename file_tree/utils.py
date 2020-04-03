from os import listdir
from os.path import isdir as is_dir

def is_hidden(path):
    ''' Check if path is a hidden file or directory. '''
    return path.split("/")[-1].startswith(".")


def contents(top_path,include_files=True,include_hidden=False):
    '''
    Returns a list with the paths of the immediate contents of top_path directory.
    If top_path is a file, returns an empty list.

    Keyword arguments:
    include_files : whether include files or only directories.
    include_hidden : whether include hidden files and hidden directories
    '''
    return [top_path+"/"+i for i in listdir(top_path)
                    if ((is_dir(top_path+"/"+i) or include_files) and
                        (not is_hidden(top_path+"/"+i) or include_hidden))] \
						if is_dir(top_path) else []

def deep_contents(top_path,include_files=True,include_hidden=False):
    '''
    Returns a list with all the contents and subcontents of top_path directory, at all levels.
    If top_path is a list, return an empty list.
    '''
    to_check = contents(top_path,include_files,include_hidden)
    checked = []

    while len(to_check)>0:
        for path in to_check:
            to_check += contents(path,include_files,include_hidden)
            to_check.remove(path)
            checked.append(path)

    return [top_path]+checked
