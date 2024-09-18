import subprocess
from subprocess import CompletedProcess
from typing import List

TEST_TEXT_FILE = "test.txt"


class TestWcc:
    """Test class containing tests related wcc CLI tool"""

    def test_all_counts(self):
        """Test all counts functionality against wc command when no options are provided"""
        self._run_and_assert(TEST_TEXT_FILE)

    def test_all_counts_stdin(self):
        """Test all counts functionality against wc command when no options are provided with stdin input"""
        self._run_and_assert(TEST_TEXT_FILE, is_stdin=True)

    def test_line_count(self):
        """Test the line count functionality against wc command."""
        self._run_and_assert(TEST_TEXT_FILE, option="-l")

    def test_word_count(self):
        """Test the word count functionality against wc command."""
        self._run_and_assert(TEST_TEXT_FILE, option="-w")

    def test_char_count(self):
        """Test the character count functionality against wc command."""
        self._run_and_assert(TEST_TEXT_FILE, option="-m")

    def test_byte_count(self):
        """Test the byte count functionality against wc command."""
        self._run_and_assert(TEST_TEXT_FILE, option="-c")

    def test_multiple_files(self):
        """Test the functionality with multiple files against wc command."""
        self._run_and_assert(TEST_TEXT_FILE, TEST_TEXT_FILE, option="-lw")

    def _run_and_assert(
        self, *file_paths: str, option: str = "", is_stdin: bool = False
    ):
        wcc_result = self._run_wcc_command(
            *file_paths, option=option, is_stdin=is_stdin
        )
        wc_result = self._run_wc_command(*file_paths, option=option, is_stdin=is_stdin)
        assert wcc_result.returncode == 0
        assert wc_result.returncode == 0
        assert wcc_result.stdout.strip() == wc_result.stdout.strip()

    def _run_wcc_command(
        self, *file_paths: str, option: str = "", is_stdin: bool = False
    ) -> CompletedProcess[str]:
        if is_stdin:
            with open(*file_paths) as f:
                return self._run_command(
                    ["python", "wcc.py", option], input_data=f.read()
                )
        return self._run_command(["python", "wcc.py", option, *file_paths])

    def _run_wc_command(
        self, *file_paths: str, option: str = "", is_stdin: bool = False
    ) -> CompletedProcess[str]:
        if is_stdin:
            with open(*file_paths) as f:
                return self._run_command(["wc", option], input_data=f.read())
        return self._run_command(["wc", option, *file_paths])

    @staticmethod
    def _run_command(command: List[str], input_data: str = "") -> CompletedProcess[str]:
        """Helper function to run a command and capture its output."""
        command = [c for c in command if c]
        result = subprocess.run(
            command, capture_output=True, text=True, input=input_data
        )
        return result
