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
    mkdir      v0.3
    rm
    rmdir
Versions:
    Alpha:
        0.0 created initial structure
        0.1 fixed cd command by using os.chdir
        0.2 fixed fatal NameError in ls command by using os.path.realdir('.')
        0.3 adding mkdir
        0.3.1 fixed mkdir--changed from [:7] to [:6]
        0.4 fixed ls command of showing other directories
        0.5 fixed ls command error responce of non-existant directory
        0.6 added get_args function to get the arguments for commands
        
"""

def get_args(string):
    args=[]
    end=''
    possible = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    ready=False
    for i in range(1,len(string)):
        if string[i]== '-' and string[i-1]== ' ':
            end+=' '
            ready=True
            continue
        if ready==True:
            if string[i] in possible:
                args.append(string[i])
                
            else:
                end+=string[i]
                ready=False
            
    return args,end
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
                try:os.chdir(command[3:])
                except:pass
        elif command == 'cd':
            try:
                file=open(os.path.join(infodir,'hmdir'))
                hmdir=file.read()
            except:
                print("No homedir given.")
                print("Please give a homir.")
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
                try:os.chdir(hmdir)
                except:pass
        elif command == 'ls' :
            for i in os.listdir(os.path.realpath('.')):
                print("%s"%i, end='\n')
            print()
        elif command[0:3] == 'ls ':
            args,string=get_args(command[3:])
            if os.path.exists(command[3:]):
##                print("Dir %s exists"%command[3:])##Testing
                startdir=os.path.realpath('.')
                try:os.chdir(command[3:])
                except Exception as E:
                    print("Error: %s"%E)
                    continue
                for i in os.listdir(os.path.realpath('.')):
                    print("%s"%i, end='\n')
                    
                os.chdir(startdir)
            elif command[3:]=='':
                for i in os.listdir(os.path.realpath('.')):
                    print("%s"%i, end='\n')
                print()
            else:
                print("Path \"%s\" not found.  "%command[3:])
            
        elif command[0:6] =='mkdir ':
            try:
                os.mkdir(command[6:].strip())
                print("Created dir: \"%s\""%command[6:].strip())
            except:
                print("Error: could not create directory")
        else:print("Command not recognized")
        
run()