#!/usr/bin/python3
"""Define Base class
"""


import json
import csv


class Base:
    """Define Base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initialisation
        Args:
            id (int, None): integer identification. Defaults to None.
        """
        if id:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
            