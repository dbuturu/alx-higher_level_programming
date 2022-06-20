#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    my_list_3 = []
    for i in range(0, list_length):
        try:
            quotient = my_list_1[i] / my_list_2[i]
        except TypeError:
            print("wrong type")
            quotient = 0
        except ZeroDivisionError:
            print("division by 0")
            quotient = 0
        except IndexError:
            print("out of range")
            quotient = 0
        finally:
            my_list_3.append(quotient)
    return my_list_3
