#!/usr/bin/python3
# 12-fizzbuzz.py

def fizzbuzz():
    """print the num from 1 to 100 separated by a space.

    for multiples of three, print Fizz instead of the num.
    for multiples of five, print Buzz instead of the num.
    for multiples of three and five, print FizzBuzz instead of the num
    """

    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz", end="")
        elif num % 3 == 0:
            print("Fizz", end="")
        elif num % 5 == 0:
            print("Buzz", end="")
        else:
            print("{}".format(num), end="")

