"""This module provides the DR Tree CLI."""

import argparse
import pathlib
import sys

from src import __version__ as version
from src.treemanager.tree import FolderTree


def parse_cmd_line_arguments():
    parser = argparse.ArgumentParser(
        prog='tree',
        description='DR Tree, a directory tree generator',
        epilog='Thanks for using DR Tree!'
    )
    parser.version = f'DR Tree v{version}'
    parser.add_argument('-v', '--version', action='version')
    parser.add_argument(
        'root_dir',
        metavar='ROOT_DIR',
        nargs='?',
        default='.',
        help='Generate a full directory tree starting at ROOT_DIR'
    )
    return parser.parse_args()


def main():
    args = parse_cmd_line_arguments()
    root_dir = pathlib.Path(args.root_dir)
    if not root_dir.is_dir():
        print('The specified root directory does not exist')
        sys.exit()
    folder_tree = FolderTree(root_dir)
    folder_tree.generate()


if __name__ == '__main__':
    main()
