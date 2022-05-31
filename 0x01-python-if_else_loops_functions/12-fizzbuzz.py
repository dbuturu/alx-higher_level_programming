#!/usr/bin/python3
def fizzbuzz():
    for x in range(1, 101):
        if x % 3 == 0 and x % 5 == 0:
            print("FizzBuzz ", end='')
            continue
        if x % 3 == 0:
            print("Fizz ", end='')
            continue
        elif x % 5 == 0:
            print("Buzz ", end='')
            continue
        else:
            print("{} ".format(x),  end='')
