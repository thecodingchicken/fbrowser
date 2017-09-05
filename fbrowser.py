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
    os.chdir
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
        0.1a fixed cd command by using os.chdir
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
    infodir=os.path.realpath('.')
    while command!='exit':
        command=input("%s$ "%os.getcwd())#os.path.realpath('.'))
        if command[0:3] == 'cd ':
            if (os.path.exists(os.path.join('.',command[3:].strip()))):
                os.chdir(command[3:])
        elif command == 'cd':
            try:
                file=open(os.path.join(infodir,'hmdir'))
                hmdir=file.read()
            except:
                print("No homedir given.")
                print("Please give a homedir.")
                conf='n'
                hmdir=''
                while conf.lower()!='y' or len(hmdir.strip())==0:
                    hmdir=input("Homedir: ")
                    print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                          end='  ')
                    conf=input("(Y/n)")
                file = open(os.path.join(infodir,'hmdir'),'w')
                file.write(hmdir)
                file.close()
                os.chdir(hmdir)
        elif command == 'ls' :
            for i in os.listdir(start):
                print("%s"%i, end='  ')
            print()
        elif command[0:3] == 'ls ':
            if os.path.exists(command[3:]):
                os.listdir(command[3:])
run()
