#!/usr/bin/python3
"""Implements review.py"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Inherits from base class"""
    place_id = ""
    user_id = ""
    text = ""
