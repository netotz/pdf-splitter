from dataclasses import dataclass
from typing import List, Tuple

from PyPDF2 import PdfFileReader, PdfFileWriter

@dataclass
class SplitFile:
    filename: str
    pages: Tuple[int, int]

    def get_range(self) -> range:
        return range(self.pages[0], self.pages[1] + 1)

def split_pdf(filename: str, splits: List[SplitFile]) -> None:
    original = PdfFileReader(filename)
    for split in splits:
        output = PdfFileWriter()
        for page_number in split.get_range():
            output.addPage(original.getPage(page_number))
        with open(f'{split.filename}.pdf', 'wb') as file:
            output.write(file)
