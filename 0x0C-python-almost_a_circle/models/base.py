#!/usr/bin/python3
"""class definition"""
import json


class Base:
    """defines class base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """instantiate id"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            return []
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = str(cls.__name__) + ".json"
        with open(file_name, mode='w') as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                for obj in list_objs:
                    obj_dict = obj.to_dictionary()
                    jsonfile.write(Base.to_json_string(obj_dict))

    @staticmethod
    def from_json_string(json_string):
        if len(json_string) == 0:
            return []
        return (json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            obj = cls(4, 5)
        elif cls.__name__ == "Square":
            obj = cls(5)
        r2.update(**dictionary)
        return obj

    @classmethod
    def load_from_file(cls):
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, mode='r') as jsonfile:
               dict_list = Base.from_json_string(jsonfile.read())
               return [cls.create(**d) for d in dict_list]
        except IOError:
            return []
      






















