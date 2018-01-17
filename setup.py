#!/bin/bash python3
"setup.py for text_file_browser"
from distutils.core import setup
import py2exe
print("IMPORTED MODULES")
try:
    setup(name=r'text_file_browser',
         version=r'2.7.5 final',
         author=r"Joshua Bowe",
         author_email=r"joshuadbowe@gmail.com",
         url=r"https://github.com/thecodingchicken",
         py_modules = ['fbrowser', 'find_file_path', 'get_args',
                       'other_functions', 'remove_comments',
                       'tarb', 'text_editor', 'zipbrowser'],
         console=r"fbrowser.py"
        )
except Exception as e:
    print ("Error: %s"%e)