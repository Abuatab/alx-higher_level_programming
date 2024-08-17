#!/usr/bin/python3
"""Defines a class MyInt that inherits from int"""


class MyInt(int):
    """A rebel int that inverts the == and != operators."""

    def __eq__(self, other):
        """Override the == operator to behave like !=."""
        return super().__ne__(other)

    def __ne__(self, other):
        """Override the != operator to behave like ==."""
        return super().__eq__(other)
