from typing import BinaryIO

from models import FileDetails


class WcCounter:
    def __init__(self, args):
        self.args = args

    def count(self, f: BinaryIO, file_details: FileDetails):
        """Count the lines, words, characters, and bytes in a binary file."""
        for line in f.readlines():
            if self.args.l:
                file_details.line_count += 1
            if self.args.c:
                file_details.byte_count += len(line)
            line = line.decode("utf-8")
            if self.args.m:
                file_details.char_count += len(line)
            if self.args.w:
                file_details.word_count += len(line.split())
