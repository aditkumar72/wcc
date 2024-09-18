from models import FilesDetails, FileDetails

MAX_POSSIBLE_WIDTH = 8
MIN_POSSIBLE_WIDTH = 1


class Printer:
    def __init__(self, args, files_details: FilesDetails):
        self.args = args
        self.files_details = files_details

    def print(self) -> None:
        """Print the details of each file and the total counts if there are multiple files."""
        for file in self.files_details.details:
            self._print(file)
        if len(self.files_details.details) > 1:
            self._print(self.files_details.total_count())

    def _print(self, file: FileDetails) -> None:
        """Prints the details of a single file or an error message if the file does not exist."""
        if not file.is_exists:
            print(f"wcc: {file.filename}: open: No such file or directory")
            return
        output = []
        if self.args.l:
            output.append(f"{self._get_space(file.line_count)}{file.line_count}")
        if self.args.w:
            output.append(f"{self._get_space(file.word_count)}{file.word_count}")
        if self.args.c:
            output.append(f"{self._get_space(file.byte_count)}{file.byte_count}")
        if self.args.m:
            output.append(f"{self._get_space(file.char_count)}{file.char_count}")
        if file.filename:
            output.append(f" {file.filename}")
        print("".join(output))

    @staticmethod
    def _get_space(num: int) -> str:
        """Get space to prepend based on num width"""
        return f"{' ' * Printer._get_available_width(num)}"

    @staticmethod
    def _get_available_width(num: int) -> int:
        """Get available width excluding width taken by the number"""
        if MAX_POSSIBLE_WIDTH <= len(str(num)):
            return MIN_POSSIBLE_WIDTH
        return MAX_POSSIBLE_WIDTH - len(str(num))
