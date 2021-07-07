import argparse

from editor import InputFile, SplitFile, split_pdf

parser = argparse.ArgumentParser()
parser.add_argument(
    'filepath',
    type=str,
    help="absolute path of the input PDF file to split, or just its name if it's in the same folder"
)
parser.add_argument(
    '-s', '--split-name',
    action='append',
    required=True,
    help="name of a split file, it's not needed to include the extension (.pdf)"
)
parser.add_argument(
    '-p', '--page-numbers',
    action='append',
    required=True,
    type=int,
    nargs=2,
    help='first and last page numbers to split from the input file'
)

args = parser.parse_args()
print(args)
if len(args.page_numbers) != len(args.split_name):
    raise argparse.ArgumentTypeError('specify the same number of page ranges as the number of splits.')

inputfile = InputFile(args.filepath)
splits = [SplitFile(f'{name}.pdf', pages) for name, pages in zip(args.split_name, args.page_numbers)]
split_pdf(inputfile, splits)
