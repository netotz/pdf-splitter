from argparse import ArgumentTypeError

from editor import InputFile, SplitFile, split_pdf


def split(args):
    if len(args.page_numbers) != len(args.split_name):
        raise ArgumentTypeError('specify the same number of page ranges as the number of splits.')

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


def move(args):
    pass
