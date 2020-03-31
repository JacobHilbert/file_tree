# file_tree
Python package to get the [GNU tree](https://linux.die.net/man/1/tree) functionality without recursion

## Usage

### from command line

To print a tree of the current directory (excluding hidden files and folders):

```
$ python -m file_tree
```

To print a tree of `./path/to/dir` directory:

```
$ python -m file_tree "./path/to/dir"
```
And to print a **directory** only tree you must add `-d`:

```
$ python -m file_tree "./path/to/dir" -d
```

And to print all files, including the hidden ones, add `-a`
```
$ python -m file_tree "./path/to/dir" -a
```


### prom python

you only need to import the Tree class. For example:

```
>>> from file_tree import Tree
>>> tree = Tree("./path/to/dir",only_dirs=False)
>>> tree.make_tree()
```

will print the tree with all files.

## To do

- [ ] Functionality to ignore hidden files and folders
    -  If name begins with a dot, the `__str__` must be "\r"
- [ ] Total count of directories and files
    - define a `kind_list` attribute to Tree class, compare elementwise to "file" and sum the `True`s. That's the number of files.
    - subtract that from the total to get the number of dirs.
- [ ] Option to sort apart directories and files
    - In this implementation it would require `__lt__` and `__eq__` methods for the `Node` class. Tough.
- [ ]  File limit per directory, replacing it by some files and continuity dots
    - One idea is, given a `Node` object that have more children than allowed, mark the other children as hidden files
        - but then it will not work on th all files mode.
    - maybe we could do just another attribute that messes with `Node.__str__`
- [ ] Option to save tree on a file.
    - But you could do `>>`
    - Though a `Tree.export_tree()` will be appreciated
- [ ] maybe export in dot format, or mathematica's `Graph` association format...
    - This is easier to do without recursion, since the flatten format of `Graph`: just run through the `Node`s and export their children relationship.


## example

This very repository:

```python
>>> from file_tree import Tree
>>> Tree("./file_tree",False).make_tree()
'''
file_tree
├── .editorconfig
├── .git
│   ├── COMMIT_EDITMSG
│   ├── FETCH_HEAD
│   ├── HEAD
│   ├── config
│   ├── description
│   ├── hooks
│   │   ├── applypatch-msg.sample
│   │   ├── commit-msg.sample
│   │   ├── fsmonitor-watchman.sample
│   │   ├── post-update.sample
│   │   ├── pre-applypatch.sample
│   │   ├── pre-commit.sample
│   │   ├── pre-push.sample
│   │   ├── pre-rebase.sample
│   │   ├── pre-receive.sample
│   │   ├── prepare-commit-msg.sample
│   │   └── update.sample
│   ├── index
│   ├── info
│   │   └── exclude
│   ├── logs
│   │   ├── HEAD
│   │   └── refs
│   │       ├── heads
│   │       │   └── master
│   │       └── remotes
│   │           └── origin
│   │               ├── HEAD
│   │               └── master
│   ├── objects
│   │   ├── 0a
│   │   │   └── 95843d23b80a392d7514eb56fab7cc9e71fd31
│   │   ├── 0d
│   │   │   └── 4cb3edee7cb950314472b217adad692b4c1124
│   │   ├── 12
│   │   │   └── 6e6adbd89710b650b76f76141c6f19e3edaf54
│   │   ├── 24
│   │   │   └── 13ada564956c0ccf12f7df77eb9aabc31a0937
│   │   ├── 27
│   │   │   └── a044c14a39bdd1a029574da739e874161585d2
│   │   ├── 2a
│   │   │   └── d0d725fa68c05977c7aad624e3603455bc1590
│   │   ├── 30
│   │   │   └── e0cbedf2260d8e3fa34c15e9a2bb76f14a6f27
│   │   ├── 32
│   │   │   └── 993f56ad525683181213151f2c021fd81013c5
│   │   ├── 34
│   │   │   └── 482d4a2681833bab27953f6964beb1099fbe2f
│   │   ├── 41
│   │   │   └── ecda9df26b808e358783fca1c677b047026b39
│   │   ├── 4a
│   │   │   └── d62e2d5afa9c5480271175c2ca8f83c926d007
│   │   ├── 4d
│   │   │   └── 9963d196163a284909aac8d3fd659bbcdef528
│   │   ├── 50
│   │   │   └── 8fbcaed11b6bfd42aa0bddc0e15c4e3140c4fa
│   │   ├── 53
│   │   │   └── 50cb9cabee004a6361fcc946a4bfdcefe6b924
│   │   ├── 5e
│   │   │   └── b0d5eeef27e2efecbdfa1337a76f86be35aa2d
│   │   ├── 5f
│   │   │   └── 771e659e7667960447753c8c5f1991ac3a2af2
│   │   ├── 6a
│   │   │   └── d6198a25bf7924939949ee0f46ee3d6133b648
│   │   ├── 71
│   │   │   └── 2a0623a5b038af8b870a45d59fbb9f6eaa670c
│   │   ├── 74
│   │   │   └── f4b018bddf26b9927b324353f1ce630f2f4d9b
│   │   ├── 7a
│   │   │   └── 37ac5b271c52d5ce314d67a4fc626cb02cf027
│   │   ├── 82
│   │   │   └── 6b372ebcef5fb85247d7b815b9a792cabf0a3b
│   │   ├── 84
│   │   │   └── 1b6bb491e5fdea3e7b63656097590515441158
│   │   ├── 8c
│   │   │   └── d185805df98403135d906b9e46e4e002c6aa38
│   │   ├── 8d
│   │   │   └── e7d83349a8991fc049c94161166b44323450f3
│   │   ├── 8e
│   │   │   └── 51df59c2835853433aeae78da765526cb34eee
│   │   ├── 93
│   │   │   └── 20419b956526c05286fb82450ae62d04b55e69
│   │   ├── a4
│   │   │   └── 7deb8bac9af34d5e2c473439728da24562ab95
│   │   ├── a8
│   │   │   └── e0aaac3d582450efe44ca52c8da8ed450ba790
│   │   ├── ad
│   │   │   └── a0bda2057893f9a66b32fc83a510e7079051fe
│   │   ├── be
│   │   │   └── f24eee08dc84566d884f063ccbece77da16b1f
│   │   ├── c0
│   │   │   └── 86d57bda225a5600ea9910fa945ecd8bbb9ad8
│   │   ├── c4
│   │   │   └── dd9b43a71c35f1cd3632ee6a38382d2868a7f9
│   │   ├── c8
│   │   │   └── 282f3e4deaf9b02fd9c5bb9ce518d679735a0c
│   │   ├── cf
│   │   │   └── fd3243c05547d21f34ddc9329fadb05acf8878
│   │   ├── d7
│   │   │   └── b8638b8fc6a3653c1b21d52e2924858aa138dd
│   │   ├── e4
│   │   │   └── 46305bb93bdcad948b3fceed0068a25fac047e
│   │   ├── e6
│   │   │   └── 9de29bb2d1d6434b8b29ae775ad8c2e48c5391
│   │   ├── ef
│   │   │   └── 7b4a38a47b3d2953488608bef4fd2a0bdef666
│   │   ├── info
│   │   └── pack
│   │       ├── pack-b85bd43a9c305b4c2689ac35673c7f485c6e0521.idx
│   │       └── pack-b85bd43a9c305b4c2689ac35673c7f485c6e0521.pack
│   ├── packed-refs
│   └── refs
│       ├── heads
│       │   └── master
│       ├── remotes
│       │   └── origin
│       │       ├── HEAD
│       │       └── master
│       └── tags
├── LICENSE
├── README.md
├── __init__.py
├── __main__.py
├── __pycache__
│   ├── __init__.cpython-37.pyc
│   ├── __main__.cpython-37.pyc
│   ├── contents.cpython-37.pyc
│   ├── node.cpython-37.pyc
│   └── tree.cpython-37.pyc
├── contents.py
├── node.py
└── tree.py
'''
```
