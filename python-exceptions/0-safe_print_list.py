#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i in range(x):
            try:
                item = my_list[i]
                print("{}".format(item), end="")
                count += 1
            except IndexError:
                break
        print("")
    except IndexError:
        pass

    return count