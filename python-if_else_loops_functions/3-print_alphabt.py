#!/usr/bin/python3
for letter_qe in range(ord('a'), ord('z')+1):
    if letter_qe != ord('e') and letter_qe != ord('q'):
        print(f"{chr(letter_qe)}", end='')
