#!/usr/bin/python3
"""
A module containing IO functions for a file.
"""


def write_file(filename="", text=""):
    """
    Writes a UTF-8 encoded text to a file.
    Args:
        filename (str): The name of the file to write to.
        text (str): The content to store in the file.
    Attributes:
        numofch (int) = holds the number of characters written.
    Returns:
        int: The number of characters written.

    """
    numofch = 0
    with open(filename, mode='w', encoding='utf-8') as f:
        numofch = f.write(str(text))
    return numofch
