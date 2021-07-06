import argparse

parser = argparse.ArgumentParser()
parser.add_argument(
    'filename',
    type=str,
    help='name of the input PDF file to split'
)
parser.add_argument(
    '-s', '--split-name',
    action='append',
    help="name of a split file, it's not needed to include the extension (.pdf)"
)
parser.add_argument(
    '-p', '--page-numbers',
    action='append',
    nargs=2,
    help='first and last page numbers to split from the input file'
)
args = parser.parse_args()
