#!/usr/bin/python3
"""
This function prints My name is <first name> <last name>
first_name and last_name must be strings
"""


def say_my_name(first_name, last_name=""):
    """
    Print a name
    """
    if type(first_name) != str:
        raise TypeError("first_name must be a string")
    if type(last_name) != str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
    
