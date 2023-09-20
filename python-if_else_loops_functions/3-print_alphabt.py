#!/usr/bin/python3
for letter_qe in range(97, 123):
    if letter_qe == 113 or letter_qe == 101:
        continue
    else:
        print("{:c}".format(letter_qe), end='')
