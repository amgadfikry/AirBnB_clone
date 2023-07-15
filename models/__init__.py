#!/usr/bin/python3
""" package module that entry point of package
    contain storage variable that represent unique storage
    for project
"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
