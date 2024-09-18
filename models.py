from dataclasses import dataclass, field


@dataclass
class FileDetails:
    """Class for storing filename and stats like word count, line count etc."""

    filename: str = None
    word_count: int = 0
    line_count: int = 0
    char_count: int = 0
    byte_count: int = 0
    is_exists: bool = False


@dataclass
class FilesDetails:
    """Class for storing info for all FileDetails"""

    details: list[FileDetails] = field(default_factory=list)

    def total_count(self) -> FileDetails:
        file_details = FileDetails(filename="total", is_exists=True)
        for file in self.details:
            file_details.line_count += file.line_count
            file_details.word_count += file.word_count
            file_details.char_count += file.char_count
            file_details.byte_count += file.byte_count
        return file_details
