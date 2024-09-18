HELP_TEXT_C = (
    "The number of bytes in each input file is written to the standard output. This will cancel out any prior "
    "usage of the -m option."
)
HELP_TEXT_L = (
    "The number of lines in each input file is written to the standard output."
)
HELP_TEXT_M = (
    "The number of characters in each input file is written to the standard output."
)
HELP_TEXT_W = (
    "The number of words in each input file is written to the standard output."
)
HELP_TEXT_FILE = "Input file(s) if any."
USAGE = "./wcc [-clmw] [file ...]"
DESCRIPTION = """
NAME
  wcc – word, line, character, and byte count

DESCRIPTION
  The wcc utility displays the number of lines, words, and bytes contained in each input file,
  or standard input (if no file is specified) to the standard output. A line is defined as a
  string of characters delimited by a <newline> character. Characters beyond the final <newline>
  character will not be included in the line count.

  A word is defined as a string of characters delimited by white space characters. If more
  than one input file is specified, a line of cumulative counts for all the files is displayed
  on a separate line after the output for the last file.
"""
