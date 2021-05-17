"""This module provides DR Tree main module."""

import os
import pathlib

PIPE = '|'
ELBOW = '└──'
TEE = '├──'
PIPE_PREFIX = '│   '
SPACE_PREFIX = "    "


class _TreeGenerator:
    def __init__(self, root_dir):
        self._root_dir = pathlib.Path(root_dir)
        self._tree = []

    def build_tree(self):
        self._tree_head()
        self._tree_body(self._root_dir)
        return self._tree

    def _add_directory(self, index, directory, branches_count, prefix, connector):
        self._tree.append(f'{prefix}{connector} {directory.name}{os.sep}')
        if index != branches_count - 1:
            prefix += PIPE_PREFIX
        else:
            prefix += SPACE_PREFIX

        self._tree_body(directory=directory, prefix=prefix)
        self._tree.append(prefix.rstrip())

    def _add_file(self, connector, file, prefix):
        self._tree.append(f'{prefix}{connector} {file.name}')

    def _tree_body(self, directory, prefix=''):
        branches = directory.iterdir()
        branches = sorted(branches, key=lambda branch: branch.is_file())
        branches_count = len(branches)
        for index, branch in enumerate(branches):
            connector = ELBOW if index == branches_count - 1 else TEE
            if branch.is_dir():
                self._add_directory(
                    index=index, directory=branch, branches_count=branches_count, prefix=prefix, connector=connector
                )
            else:
                self._add_file(connector=connector, file=branch, prefix=prefix)

    def _tree_head(self):
        self._tree.append(f'{self._root_dir}{os.sep}')
        self._tree.append(PIPE)


class FolderTree:
    """

    """

    def __init__(self, root_dir):
        self._generator = _TreeGenerator(root_dir)

    def generate(self):
        tree = self._generator.build_tree()
        for branch in tree:
            print(branch)
