#!/bin/bash python3
"setup.py for text_file_browser"
from distutils.core import setup
import py2exe
setup(name=r'text_file_browser',
     version=r'2.7.5 final',
     author=r"Joshua Bowe",
     author_email=r"joshuadbowe@gmail.com",
     url=r"https://github.com/thecodingchicken",
     py_modules = [r'fbrowser', r'find_file_path', r'get_args',
                   r'other_functions', r'remove_comments',
                   r'tarb', r'text_editor', r'zipbrowser'],
     console=r"fbrowser.py"
    )