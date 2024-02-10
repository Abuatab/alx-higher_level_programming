#!/usr/bin/python3
def print_last_digit(number):
    rd = abs(number) % 10
    print(rd, end="")
    return rd
