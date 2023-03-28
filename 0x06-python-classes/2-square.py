#!/usr/bin/python3
"""Example Google style docstrings.

This module demonstrates documentation as specified by the `Google Python
Style Guide`_. Docstrings may extend over multiple lines. Sections are created
with a section header and a colon followed by a block of indented text.

Example:
    Examples can be given using either the ``Example`` or ``Examples``
    sections. Sections support any reStructuredText formatting, including
    literal blocks::
"""

class Square:
    """ A class that defines a square by its size

    This defines an empty square class.
    As instructed, no method or attribute is created
    """
    def __init__(self, size=0):
        """ Method to initialize the square object

        This defines an empty square class.
        As instructed, no method or attribute is created
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = int(size)
