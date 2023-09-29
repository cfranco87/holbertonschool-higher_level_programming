#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    try:
        if len(my_list_1) != len(my_list_2):
            raise ValueError("List are not same size")

        result = []
        for a, b in zip(my_list_1, my_list_2):
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                result.append(0)  # Replace non-numeric elements with 0
            elif b == 0:
                result.append(float('inf'))  # Handle division by zero
            else:
                result.append(a / b)

        if any(element < list_length for element in result):
                print("{}".format("The elements are too damn high"))

    except ZeroDivisionError:
            print("{}".format("Division by 0"))
    finally:
        print("{}".format("Out of range"))

    return result