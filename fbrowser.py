#!/bin/bash python3
#fbrowser.py

import os
import sys
import shutil
import time
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
    mkdir      v0.3
    rm
    rmdir      v0.7
    info       v0.9
    pwd        v1.1
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
        0.7 added rmdir
        0.8 fixed rmdir with '.' and '..'
        0.8.1 added error detection in rmdir
        0.9 added info command-lists common information on files
    Beta:
       Starting comment:
          The file browser currently works, and it works well.  You can change
          directorys and such.  Currently, you can create empty directorys and
          delete empty directorys.  I will add rm in soon.
        1.0 Working on rm.
        1.0.1 Finished rm
        1.0.2 Fixed rm- brought up TypeError when it split the name rather than
                    stripping it
        1.1 Added pwd command.  
        
        
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
        elif command[0:4]=='ls2 ':
            args,string=get_args(command[3:])
            if os.path.exists(string):
                dir_listings=os.listdir(string)
                for i in range(len(dir_listing)):
                    to_print='%s\t'%dir_listing[i]
                    if 'l' in args:
                        to_print="%s\t"
        elif command[0:6] =='mkdir ':
            try:
                os.mkdir(command[6:].strip())
                print("Created dir: \"%s\""%command[6:].strip())
            except:
                print("Error: could not create directory")
        elif command[0:5]=='info ':
            if os.path.exists(command[5:].strip()):
                info=os.lstat(command[5:].strip())
##                command=[command[:5]+command[5:].strip()
                print("Name:            %s"%command[5:].strip())
                print("st_mode:         %d"%info[0])
                print("Inode number:    %d"%info[1])
                print("st_dev:          %d"%info[2])
                print("Size:            %d bytes"%info[6])
                print("st_atime:        %s"%time.ctime(info[7]))
                print("Last modified:   %s"%time.ctime(info[8]))
                print("Creation:        %s"%time.ctime(info[9]))
        elif command[0:6] == 'rmdir ':
            DIR=command[6:].strip()
            try:
                if os.path.exists(DIR):
                    os.chdir(DIR)
                    contents=os.listdir('.')
                    if len(contents) == 0:
                        os.chdir('..')
    ##                    shutil.rmtree(DIR)
                        os.rmdir(DIR)
                        print("Deleted dir: %s"%DIR)
                    else:
                        print("Directory is not empty.")
            except Exception as error:
                print("Error: %s"%error)
        elif command.find( 'exit' ) != -1:
            pass
        elif command[0:3] == 'rm ':
            if os.path.exists(command[3:].strip()):
                try:
                    os.unlink(command[3:].strip())
                except PermissionError:
                    print("Error: you cannot delete the file")
                    print("Not enough permissions")
        elif command.find( 'pwd')==0:
            print('\n\t%s\n'%os.path.realpath('.'))
        else:print("Command not recognized")
        
run()
