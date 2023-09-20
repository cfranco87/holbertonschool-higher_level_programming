#!/usr/bin/python3
for letter_qe in range(ord('a'), ord('z')+1):
    letter = chr(letter_qe)
    if letter not in "qe":
        print(letter, end='')