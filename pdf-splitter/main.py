import argparse

import actions


parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(
    title='subcommands'
)

split_subcommand = subparsers.add_parser(
    'split',
    help='splits a PDF'    
)
split_subcommand.add_argument(
    'filepath',
    type=str,
    help="absolute path of the input PDF file to split, or just its name if it's in the same folder"
)
split_subcommand.add_argument(
    '-s', '--split-name',
    action='append',
    required=True,
    help="name of a split file, it's not needed to include the extension (.pdf)"
)
split_subcommand.add_argument(
    '-p', '--page-numbers',
    action='append',
    required=True,
    type=int,
    nargs=2,
    help='range of first and last page numbers to split from the input file, according to file numbering (first page is page 1)'
)
split_subcommand.add_argument(
    '-d', '--delete',
    action='store_true',
    help='deletes the input file only if specified'
)
split_subcommand.set_defaults(
    func=actions.split
)

copy_subcommand = subparsers.add_parser(
    'copy',
    help='copies files that match the ID of a list file to another directory'
)
copy_subcommand.add_argument(
    'list',
    type=str,
    help='name of the file that contains the IDs to look for, each one in a new line'
)
copy_subcommand.add_argument(
    'destination',
    type=str,
    help='absolute path of the directory to copy the found files to'
)
copy_subcommand.add_argument(
    '-t', '--type',
    type=int,
    help='type of file to look for'
)
copy_subcommand.set_defaults(
    func=actions.copy
)

args = parser.parse_args()
args.func(args)
