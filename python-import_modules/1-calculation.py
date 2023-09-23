#!/usr/bin/python3
if __name__ == "__main__":
    from calculator_1 import add
    from calculator_1 import sub
    from calculator_1 import mul
    from calculator_1 import div

    a = 10
    b = 5
    result_add= add(a, b)
    result_sub= sub(a, b)
    result_mul= mul(a, b)
    result_div= div(a, b)
    
    print("{} + {} = {}\n".format(a, b, result_add), end="")
    print("{} + {} = {}\n".format(a, b, result_sub), end="")
    print("{} + {} = {}\n".format(a, b, result_mul), end="")
    print("{} + {} = {}\n".format(a, b, result_div), end="")
    