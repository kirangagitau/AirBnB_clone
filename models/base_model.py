#!/usr/bin/python3

import uuid
from datetime import datetime

class BaseModel:
    def __init__(self):
        """Constructor to initialize the BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Returns a dictionary containing all keys/values of __dict__ of the instance."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """Returns the string representation of the BaseModel instance."""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

# Example usage
if __name__ == "__main__":
    my_model = BaseModel()
    my_model.name = "My First Model"
    my_model.my_number = 89
    print(my_model)            # Output the string representation of the model
    my_model.save()            # Update the updated_at attribute
    print(my_model)            # Output the updated string representation of the model
    my_model_json = my_model.to_dict()  # Get the dictionary representation of the model
    print(my_model_json)       # Print the dictionary representation
    print("JSON of my_model:")
    for key in my_model_json.keys():
        print("\t{}: ({}) - {}".format(key, type(my_model_json[key]), my_model_json[key]))
