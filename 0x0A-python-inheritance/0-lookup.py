#!/usr/bin/python3
"""This function returns a list of available attributes & methods"""


def lookup(obj):
	"""Returns the list of available attributes and methods"""
	return (dir(obj))
