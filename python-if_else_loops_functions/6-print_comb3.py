#!/usr/bin/python3

for i in range(10):
    for j in range(10):
        if i != j and j > i:
            print("{0}{1}".format(i, j), end=", ")
print("{}".format(89), end="\n")
