#!/bin/bash python3
#fbrowser.py

import os
import sys
"""
Python text file browser
will use:
    os.listdir
    os.path.isdir
    os.path.isfile
    os.path.join
commands to use:
    cd         v0.0
    ls         v0.0
    list
    mkdir
    rm
    rmdir
Versions:
    Alpha:
        0.0 created initial structure
        0.1a working on cd fixes
"""

def run():
    print("Python Text File Browser.")
    print("\nA convient file browser made by Joshua")
    usern=input("Username(for history to be sent to Joshua): ")
    if len(usern)>0:
        a=open('h_file','a')
        a.write('%s\n'%usern)
        a.close()
    print("Starting browser")
    command=None
    start=os.path.realpath('.')
    while command!='exit':
        command=input("%s$ "%start)#os.path.realpath('.'))
        if command[0:3] == 'cd ':
            if (os.path.exists(os.path.join('.',command[3:].strip()))):
                print(1)
                start = os.path.join('.',command[3:].strip())
                start = os.path.realpath(start)
            elif (os.path.exists(command[3:].strip())):
                print(2)
                start= os.path.realpath(command[3:].strip())
            else:
                print(3)
                print(command[3:])
        elif command == 'ls' :
            for i in os.listdir(start):
                print("%s"%i, end='  ')
            print()
        elif command[0:3] == 'ls ':
            if os.path.exists(command[3:]):
                os.listdir(command[3:])
run()
