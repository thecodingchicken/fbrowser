"""tarb.py
Author: Joshua Bowe
A file that contains a python tar file browser interface.
Functions inside: tarb

for more help, look at the doc for tarb"""

import os
import tarfile
from other_functions import string_contains
__all__ = ['tarb']#only thing needed to use this
def show_avail_tar():
    "Show all tar files in the current directory"
    print("Tar file not found.")
    print("Other tar files are:")
    files = os.listdir('.')
    for i in enumerate(files):
        if string_contains(i[1], '.tar'):
            print(files[i[0]])
    return

def print_start_info():
    "print the starting help for the function tarb"
    print("Tar file exists.  \nDepending on the size of the file,",
          end='')
    print(" it may take a long time")
    print("Loaded tar file.  Starting tarbrowser.\n")
def tar_view(file_n):
    "list the files in a tar archive"
    file = tarfile.TarFile(file_n)
    for line_info in enumerate(file):
        print(line_info[1], end='')
        if line_info[0]%10 == 9:
            try:
                input("Press enter to continue.")
            except (KeyError, EOFError) as key_error_:
                print("Exiting because of %s"%key_error_)
                break
    file.close()
    return
def tar_add(file_n, text):
    "add a file to the tar browser"
    if os.path.exists(text[4:].strip()):
        file = tarfile.TarFile(file_n, 'a')
        print("Opened tar archive.")
        if os.path.isfile(text[4:].strip()):
            print("Adding file to archive")
            try:
                file.add(os.path.basename(text[4:].strip()))
            except FileNotFoundError:
                print("Error: File not found!")
            else:
                os.unlink(os.path.basename(text[4:].strip()))
        try:
            file.add(text[4:].strip())
        except FileNotFoundError:
            print("File %s not found"%text[4:])
        else:
            print("Wrote file/folder")
            file.close()
    else:
        print("File doesn't exist")
def tarb(file_n):
    """tarb(file_n)
    file_n must be a valid tar file"""
    if not os.path.exists(file_n):
        show_avail_tar()
        return
    print_start_info()
    text = ''
    while True:
        try:
            text = input('%s >'%os.path.basename(file_n))
        except (KeyError, EOFError):
            print("To quit, type 'exit'")
            continue
        if text == 'exit':
            print("Exiting")
            break
        elif text[:4] == 'add ':
            tar_add(file_n, text)
        elif text == 'view':
            tar_view(file_n)
    return
