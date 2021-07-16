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
    help='range of first and last page numbers to split from the input file, according to file numbering (first page is page 1)'
)
parser.add_argument(
    '-d', '--delete',
    action='store_true',
    help='deletes the input file only if specified'
)

args = parser.parse_args()
if len(args.page_numbers) != len(args.split_name):
    raise argparse.ArgumentTypeError('specify the same number of page ranges as the number of splits.')

inputfile = InputFile(args.filepath)
splits = [
    SplitFile(f'{inputfile.id}-{name}.pdf', pages)
    for name, pages in zip(
        args.split_name,
        # PDF objects number pages starting in 0
        ((first - 1, last - 1) for first, last in args.page_numbers)
    )
]

# info in console
print(f'Splitting {inputfile.name} into {len(splits)} new files...', flush=True)
split_pdf(inputfile, splits, args.delete)
print(f'{len(splits)} files created:', flush=True)
for split in splits:
    print(f' - {split.name}')
