# PDF splitter

A simple command line tool to split a PDF file according to the pages content.

## Motivation

This project is the solution to automate a process that I was doing completely manually.
There are 3 folders, each containing ~250 PDF files. Each file contains one or many documents of a person, and they need to be split into different files each of which has a new name according to a format,
e.g. a file is named `1234.pdf` where `1234` is the ID of the person. This file contains the person's degree in the first 2 pages and the ID card in the 3rd page.
So the degree will be extracted from pages 1 and 2 and named `1234-DEGREE-BACH.pdf`, assuming it's a bachelor's, and the ID card from page 3 with name `1234-IDCARD.pdf`.

The original files don't follow a guideline, thus it's not possible to anticipate the order of the person's documents or if any of them is present at all, so I could only think about automatizing the process of splitting and naming the new files.
As a result, I developed a simple CLI specifically for this problem.

After the previous task was done, another one came up: to search for PDF files of some persons, specified by their IDs, and then splitting them following the same guideline as the previous goal.
There's a web UI to search the person by typing her/his ID, scroll to a section of files, and select a couple of options to finally see the PDF... lots of clicks, and there were ~200 IDs.

I have access to the directory that contains the files, so I decided to convert the original one-command tool into a subcommands tool (this README is updated to show it like that), adding a new subcommand to search inside the directory the files that I needed and copy them to a local folder.
This directory has +60 000 folders and +600 000 files in total.

## Usage

If you run [`main.py`](/pdf-splitter/main.py) using the `--help` argument you'll see the following:

```txt
$ py main.py -h
usage: main.py [-h] {split,copy} ...

optional arguments:
  -h, --help    show this help message and exit

subcommands:
  {split,copy}
    split       splits a PDF
    copy        copies files that match the ID of a list file to another directory
```

### `split` subcommand

```txt
$ py main.py split -h
usage: main.py split [-h] -s SPLIT_NAME -p PAGE_NUMBERS PAGE_NUMBERS [-d] filepath

positional arguments:
  filepath              absolute path of the input PDF file to split, or just its name if it's in the same folder

optional arguments:
  -h, --help            show this help message and exit
  -s SPLIT_NAME, --split-name SPLIT_NAME
                        name of a split file, it's not needed to include the extension (.pdf)
  -p PAGE_NUMBERS PAGE_NUMBERS, --page-numbers PAGE_NUMBERS PAGE_NUMBERS
                        range of first and last page numbers to split from the input file, according to file numbering (first page is page 1)
  -d, --delete          deletes the input file only if specified
```

#### Arguments

Arguments `-s` and `-p` are required can be repeated as many times as needed, but both have to be repeated the same number of times.
So if a file needs to be split into 3 new files, 3 file names will need to be specified, each one with `-s`, and also 3 page ranges with `-p`, respectively.

In my case, the original file it's not needed after being split, hence I use argument `-d` to delete it.
It's optional, so the input file will remain there if not specified.

### `copy` subcommand

```txt
$ py main.py copy -h
usage: main.py copy [-h] [-t TYPE] list destination

positional arguments:
  list                  name of the file that contains the IDs to look for, each one in a new line
  destination           absolute path of the directory to copy the found files to

optional arguments:
  -h, --help            show this help message and exit
  -t TYPE, --type TYPE  type of file to look for
```

### Executables

I'm using a Windows executable generated with [`PyInstaller`](https://github.com/pyinstaller/pyinstaller), which is available in [Releases](https://github.com/netotz/pdf-splitter/releases), because the client PC containing the PDFs folder doesn't have Python installed.
There are versions for both 64-bit and 32-bit CPUs, because my PC is 32-bit.
If you want to generate the executables yourself, there's a bash script [`genexes.sh`](/genexes.sh) that runs `pyinstaller` with arguments I personally prefer:

```txt
$ bash genexes.sh
```

If you open the script you'll see that you'll need to create two [virtual environments](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment),
one using a Python version for 64-bit, and the other one with a version for 32-bit, so you would need to have both versions installed.

### Examples

#### Splitting a PDF

Assume this is the folder, and you're using the executable:

```txt
folder/
├─ pdf-splitter.exe
├─ 1234.pdf
```

Following the previous example, running this inside `folder/`:

```txt
pdf-splitter split -s DEGREE-BACH -s IDCARD -p 1 2 -p 3 3 1234.pdf
```

Will result in:

```txt
folder/
├─ pdf-splitter.exe
├─ 1234.pdf             - 3 pages
├─ 1234-DEGREE-BACH.pdf - 2 pages
├─ 1234-IDCARD.pdf      - 1 page
```

#### Copying PDFs

Suppose we have the following file `list.txt`:

```txt
100100
150000
202202
...
```

Given the following directory, we want to copy the files that end in `15`:

```txt
Archivos/
├─ 100a199/
│  ├─ 0100100/
│  │  ├─ 0100100-8.pdf
│  │  ├─ 0100100-15.pdf   <---
│  ├─ 0150000/
│  │  ├─ 0150000-15.pdf   <---
│  │  ├─ ...
│  ├─ ...
├─ 200a299/
│  ├─ 0202202/
│  │  ├─ 0202202-2.pdf
│  │  ├─ 0202202-15.pdf   <---
│  │  ├─ ...
│  ├─ ...
├─ ...
├─ pdf-splitter.exe
├─ list.txt
```

_Archivos_ means _Files_, each subfolder is a range of the first three digits of a six digits number, _a_ means _to_ (yeah the structure is horrible lol I didn't make it).

```txt
pdf-splitter copy list.txt D:\Copiados -t 15
```

```txt
Copiados/
├─ 0100100-15.pdf
├─ 0150000-15.pdf
├─ 0202202-15.pdf
├─ ...
```
