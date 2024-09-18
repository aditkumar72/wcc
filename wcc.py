import argparse
import sys

from printer import Printer
from wccounter import WcCounter
from helptexts import *
from models import FileDetails, FilesDetails


def main():
    parser = argparse.ArgumentParser(
        usage=USAGE,
        description=DESCRIPTION,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("-c", action="store_true", help=HELP_TEXT_C)
    parser.add_argument("-l", action="store_true", help=HELP_TEXT_L)
    parser.add_argument("-m", action="store_true", help=HELP_TEXT_M)
    parser.add_argument("-w", action="store_true", help=HELP_TEXT_W)
    parser.add_argument("files", nargs="*", help=HELP_TEXT_FILE)

    args = parser.parse_args()

    # count line, words, bytes if no flags mentioned
    if not (args.c or args.l or args.m or args.w):
        args.c = args.l = args.m = args.w = True
    # give priority to counting bytes if both bytes and character count are requested
    if args.c and args.m:
        args.m = False

    files_details = FilesDetails()
    counter = WcCounter(args)
    if args.files:
        for file_name in args.files:
            file_details = FileDetails(filename=file_name)
            try:
                with open(file_name, mode="rb") as f:
                    file_details.is_exists = True
                    counter.count(f, file_details)
            except FileNotFoundError:
                pass
            files_details.details.append(file_details)
    else:
        file_details = FileDetails()
        file_details.is_exists = True
        counter.count(sys.stdin.buffer, file_details)
        files_details.details.append(file_details)

    printer = Printer(args=args, files_details=files_details)
    printer.print()


main()
