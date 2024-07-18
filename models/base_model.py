#!/usr/bin/python3

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """ this is the base model for the AirBnB clone project"""
    def __init__(self):
        """Constructor to initialize the BaseModel instance."""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.utcnow()
        self.updated_at = datetime.utcnow()

    def save(self):
        """Updates the updated_at attribute with the current datetime."""
        self.updated_at = datetime.utcnow()

    def to_dict(self):
        """Rtrn dict keys/values of __dict__ of the instance."""
        inst_dict = self.__dict__.copy()
        inst_dict["__class__"] = self.__class__.__name__
        inst_dict["created_at"] = self.created_at.isoformat()
        inst_dict["updated_at"] = self.updated_at.isoformat()
        return inst_dict

    def __str__(self):
        """Rtrn str representation of the BaseModel instance."""
        cname = self.__class__.__name__
        return "[{}] ({}) {}".format(cname, self.id, self.__dic__)
