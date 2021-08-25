from argparse import ArgumentTypeError
import os
import shutil

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


def copy(args):
    with open(args.list, 'r') as listfile:
        ids_str = listfile.read().splitlines()

    if not os.path.exists(args.destination):
        os.mkdir(args.destination)

    for id in ids_str:
        idint = int(id)
        first_digit = idint // 10 ** 5
        minid = first_digit * 100
        maxid = minid + 99
        rangedir = f'{minid}a{maxid}'
        
        zerosid = '0' * (7 - len(id)) + id
        filename = f'{zerosid}-{args.type}.pdf'

        source = os.path.join(rangedir, zerosid, filename)
        if not os.path.exists(source):
            print(f"! - File {source} doesn't exist")
            continue

        destination = os.path.join(args.destination, filename)
        
        print(f'Copying {source}\n\t-> {destination}...', flush=True)
        shutil.copy(source, destination)
