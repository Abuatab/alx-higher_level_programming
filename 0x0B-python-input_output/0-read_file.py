#!/usr/bin/pyhton3
"""Defines a function that reads and prints a file"""


def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout"""
    with open(filename, encoding='utf-8') as f:
        f_contents = f.read()
        print(f_contents)


read_file('my_file_0.txt')
