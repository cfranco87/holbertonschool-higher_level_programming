#!/usr/bin/python3
"""
Creating Class Base
"""
import json
from os import path


class Base:
    """
    this will be out base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        convert a list of dictionaries to a JSON string
        """
        if list_dictionaries is None or not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Class method for list_objs
        """
        filename = "{}.json".format(cls.__name__)
        list_dic = []

        if not list_objs:
            pass
        else:
            for i in range(len(list_objs)):
                list_dic.append(list_objs[i].to_dictionary())

        lists = cls.to_json_string(list_dic)

        with open(filename, 'w') as f:
            f.write(lists)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns: Instance with all attributes already set
        """
        if cls.__name__ == "Rectangle":
            r = cls(1, 1)
        else:
            r = cls(1)
        r.update(**dictionary)
        return r

    @classmethod
    def load_from_file(cls):
        """Returns: List of instances"""
        filename = cls.__name__ + ".json"
        my_list = []

        if path.isfile(filename):
            with open(filename) as f:
                list_output = cls.from_json_string(f.read())
            for e in list_output:
                my_list.append(cls.create(**e))
        return my_list

    @staticmethod
    def from_json_string(json_string):
        """
        convert a list of dictionaries to a JSON string
        """
        if json_string is None or not json_string:
            return []
        return (json.loads(json_string))
