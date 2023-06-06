#!/usr/bin/python3
# 9-print_last_digit.py

def print_last_digit(num):
    """print the last digit of the num and return it."""
    print(abs(num) % 10, end="")
    return (abs(num) % 10)
