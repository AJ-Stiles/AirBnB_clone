#!/usr/bin/python3
"""
models package: Initializes the FileStorage instance.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
