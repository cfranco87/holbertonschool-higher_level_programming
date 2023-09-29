try:
        if len(my_list_1) != len(my_list_2):
            raise ValueError("List are not the same size")

        result = []
        for a, b in zip(my_list_1, my_list_2):
            try:
                if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                    raise TypeError("wrong type")
                elif b == 0:
                    raise ZeroDivisionError("Division by 0")      
                else:
                    result.append(a / b)
            except TypeError:
                print("{}".format("Wrong type"))
                result.append(0)
            except ZeroDivisionError:
                print("{}".format("Division by 0"))
                result.append(0)

        if len(result) < list_length:
            raise ValueError("Out of range")
    except ValueError as e:
        print(e)        
    finally:
        print("Function execution complete")

    return result