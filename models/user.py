#!/usr/bin/python3
"""Implements all users functionalities"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Inherits from BaseModel

    Args:
        email (str): user's email
        password (srr): user's password
        first_name (str): user's first name
        last_name (str): user's last name
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
