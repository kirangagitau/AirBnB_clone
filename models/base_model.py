#!/usr/bin/python3
"""
Use pyhton version 3
this class is the base for other classes & we can inherit attributes
and common functionalities
"""
import uuid
from datetime import datetime


class BaseModel:
    def __init__(self):  # constructor to base model
        self.id = str(uuid.uuid4())

        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """
        method to mark when object/instance was last updated
        """
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """
        make a copy & create a akey
        """
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()

        return inst_dict

    def __str__(self):
        """
        method for string representation of class
        """
        class_name = self.__class__.__name__
        """
        return a formated string for
        """
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)


if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)
    my_model.save()
    print(my_model)
    my_model_json = my_model.to_dict()
    print(my_model_json)
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
