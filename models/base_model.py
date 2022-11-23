#!/usr/bin/python3
"""BaseModel Class"""
import uuid
from datetime import datetime


now = datetime.now()
class BaseModel:
    "Create the BaseMdel Class"
    def __init__(self, *args, **kwargs):
        """Initilize public instance attributes
        
            args(list): Empty list
            kwargs(dict): dictionary that contain key/value of the attirbutes
        """
        # **kwargs
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == 'created_at':
                    value = datetime.fromisoformat(value)
                elif key == 'updated_at':
                    value = datetime.fromisoformat(value)
                if key == '__class__':
                    continue
                setattr(self, key, value)
        else:
            id = uuid.uuid4()
            self.id = str(id)
            self.created_at = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
            self.updated_at = self.created_at

    def save(self):
        """updates the public instance attribut update_at with the current datetime"""
        self.updated_at = now.strftime("%Y-%m-%dT%H:%M:%S.%f")
    
    def to_dict(self):
        """Returns dictionary containing all keys/values of the instance:"""
        self.__dict__['__class__'] = self.__class__.__name__
        return self.__dict__

    def __str__(self):
        """Return Representation of the Ojbect [<class name>] (<self.id>) <self.__dict__>"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

