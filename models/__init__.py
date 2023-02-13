#!/usr/bin/python3
"""
Creates a file storage instance
"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
