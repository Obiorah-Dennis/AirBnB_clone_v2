""" module for class Review that inherits from BaseModel """
from models.base_model import BaseModel


class Review(BaseModel):
    """ Review class """
    place_id = ""
    user_id = ""
    text = ""
