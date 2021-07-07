from dataclasses import dataclass
from typing import List, Tuple
from pathlib import Path
import re

from PyPDF2 import PdfFileReader, PdfFileWriter

class InputFile:
    def __init__(self, rawpath: str) -> None:
        self.path = Path(rawpath)
        self.abspath = self.path.as_posix()
        self.name = self.path.name
        self.id = re.match(r'^\d+', self.name).group()

@dataclass
class SplitFile:
    name: str
    pages: Tuple[int, int]

    def get_pages_range(self) -> range:
        return range(self.pages[0], self.pages[1] + 1)

def split_pdf(inputfile: InputFile, splits: List[SplitFile]) -> None:
    original = PdfFileReader(inputfile.abspath)
    for split in splits:
        output = PdfFileWriter()
        for page_number in split.get_pages_range():
            output.addPage(original.getPage(page_number))
        with open(f'{inputfile.id}-{split.name}', 'wb') as file:
            output.write(file)
