# PDF splitter

A simple command line tool to split a PDF file according to the pages content.

## Motivation

This project is the solution to automate a process that I was doing completely manually.
There is a folder that contains ~250 PDF files. Each file contains one or many documents of a person, and they need to be split into different files each of which has a new name according to a format,
e.g. a file is named `1234.pdf` where `1234` is the ID of the person. This file contains the person's degree in the first 2 pages and the ID card in the 3rd page.
So the degree will be extracted from pages 1 and 2 and named `1234-DEGREE-BACH.pdf`, assuming it's a bachelor's, and the ID card from page 3 with name `1234-IDCARD.pdf`.

The original files don't follow a guideline, thus it's not possible to anticipate the order of the person's documents or if any of them is present at all, so I could only think about automatizing the process of splitting and naming the new files.
As a result, I developed a simple CLI specifically for this problem.

If you run [`main.py`](/pdf-splitter/main.py) using the `--help` argument you'll see the following:

```txt
$ py pdf-splitter/main.py -h
usage: main.py [-h] -s SPLIT_NAME -p PAGE_NUMBERS PAGE_NUMBERS filepath

positional arguments:
  filepath              absolute path of the input PDF file to split, or just its name if it's in the same folder

optional arguments:
  -h, --help            show this help message and exit
  -s SPLIT_NAME, --split-name SPLIT_NAME
                        name of a split file, it's not needed to include the extension (.pdf)
  -p PAGE_NUMBERS PAGE_NUMBERS, --page-numbers PAGE_NUMBERS PAGE_NUMBERS
                        first and last page numbers to split from the input file
```

### Usage

I'm using a Windows executable generated with [`PyInstaller`](https://github.com/pyinstaller/pyinstaller), which is available in [Releases](https://github.com/netotz/pdf-splitter/releases), because the client PC containing the PDFs folder doesn't have Python installed.

Arguments `-s` and `-p` can be repeated as many times as needed, but both have to be repeated the same number of times.
So if a file needs to be split into 3 new files, 3 file names will need to be specified, each one with `-s`, and also 3 page ranges with `-p`, respectively.

The page numbers start in 0.

### Examples

Assume this is the folder, and you're using the executable:

```txt
folder/
├─ pdf-splitter.exe
├─ 1234.pdf
```

Following the previous example, running this inside `folder/`:

```txt
pdf-splitter -s DEGREE-BACH -s IDCARD -p 0 1 -p 2 2 1234.pdf
```

Will result in:

```txt
folder/
├─ pdf-splitter.exe
├─ 1234.pdf             - 3 pages
├─ 1234-DEGREE-BACH.pdf - 2 pages
├─ 1234-IDCARD.pdf      - 1 page
```
