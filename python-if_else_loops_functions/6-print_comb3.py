#!/usr/bin/python3

for i in range (10):
    for j in range(10):
        if(i!=j):
            if(j>i):
                print(f"{i}{j}", end=", ")
print(f"89")