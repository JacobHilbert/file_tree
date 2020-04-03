# file_tree
Python package to get the [GNU tree](https://linux.die.net/man/1/tree) functionality without recursion.

## Installation

Download this repository, open a terminal on it, and run:

```
$ pip install -e .
```

## Usage

### from command line

`python -m file_tree` will print the drectori and file tree structure of the current path.

`python -m file_tree "path/to/dir" -d -h` will print a directory-only (`-d`) path tree includin all hidden paths (`-h`). `-d` and `-h` are combianble.

### prom python

You only need to import the Tree class:

```python
>>> from file_tree import Tree
>>> print(Tree("./path/to/dir",include_files=True,include_hidden=True)) # this will print the tree
```



## Structure

### `utils.py`

- `contents(top_path,include_files=True,include_hidden=False)`:

  gives the immediate contents of the `top_path` directory. If it's a file, returns `[]`.

  Args:

  * `top_path`
  * `include_files`: If False, gives only directory contents. If True, all contents.
  * `include_hidden`: If False, exclude all directories and files that begins with `.`

- `deep_contents(top_path,include_files=True,include_hidden=False)`:

  gives the contents of `top_path` at all levels. If it's a file, returns `[]`

  Args same as `contents`

### `node.py`, `Node` class

#### Attributes:

- `path`
- `splitted`
- `name`
- `level`
- `is_last`
- `kind`
- `children`

#### Methods

- `__init__(path)`
    * Only to set attributes
- `__repr__()`
    * "Node {name} on {path}, {len(children)} children"
- `__str__()`
    * return the sum of `splitted`
- `value()`
	* return... the path, except every object has pre-attached its kind. This construct seems to work out the file-dir sorting.
- `__lt__(other)`
	* comparing values sorta works (?)

### `tree.py`, `Tree` class

#### Attributes

- `include_files`
- `include_hidden`
- `root` (the top_path)
- `nodes` (node's list)
- `node_dict` {path:node}

#### Methods

- `__init__(top_path,include_files=True,include_hidden=False)`
    - Set attributes
        - hopefully `utils.deep_contents(...)` will figure this out.
        - It may be a bug on sorting the nodes...
        - That includes filling the dict.
    - Calls `register_children(node)` for each node
    - Calls `format_node` for each node.
- `__repr__()`
- `__str__()`
    - Collects all the string form of nodes
    - Calls `kind_count` and append it at the end.
- `register_nodes_children()`
    - only one node.
    - sort the list **after** created, in accordance to `Node.__lt__` implementation.
- `format_node(node)`
    - for the other nodes...
        - all of them, it takes no time time to rule the others out
    - compare the paths
        - and the last children's formatting rule, which may cause an exception, ignore it
    - format accordingly
    - run through the current node children
        - add "tees". More of a Korean /a/ though.
        - fix last one with an "ell"
- `export_association()`
    - run through all nodes, export their children relation, bob's your uncle.
- `export_dot_graph()`
    - `NotImplemented` error.
- `export_tree(file)`
    - write `Tree.__str__()` to file


## example

This very repository:

```python
>>> from file_tree import Tree
>>> print(Tree())
'''
file_tree
├── file_tree
│   ├── __pycache__
│   │   ├── __init__.cpython-37.pyc
│   │   ├── node.cpython-37.pyc
│   │   ├── tree.cpython-37.pyc
│   │   └── utils.cpython-37.pyc
│   ├── __init__.py
│   ├── __main__.py
│   ├── node.py
│   ├── tree.py
│   └── utils.py
├── file_tree.egg-info
│   ├── PKG-INFO
│   ├── SOURCES.txt
│   ├── dependency_links.txt
│   └── top_level.txt
├── LICENSE
├── README.md
└── setup.py

4 directories.
16 files.
'''
```
