#!/usr/bin/python3
"""Prints the alphabets in lower case not followed by a new line"""

for letter in range(97, 123):
    print("{}".format(chr(letter)), end="")
