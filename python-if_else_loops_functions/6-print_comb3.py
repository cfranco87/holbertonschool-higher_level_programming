#!/usr/bin/python3

printed_89 = False

for i in range(10):
    for j in range(10):
        if i != j and j > i:
            print("{0}{1}".format(i, j), end=", ")
        if i == 8 and not printed_89:
            print("{}".format(89), end="\n")
            printed_89 = True 

