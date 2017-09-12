#!/bin/bash python3
#fbrowser.py
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
    rm         v1.0
    rmdir      v0.7
    info       v0.9
    pwd        v1.1
    rmtree     v1.3
    cp         v1.4
    mv         v1.5
    touch      v1.7
    cdhmdir    v1.7.1
    run        v2.0
    cat        v2.3
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
        1.2 Added rm file-not found ability; added rm help;
                    changed starting message
        1.3 Added rmtree, a function to delete directorys that contain data.
        1.4 Added cp, a command to copy over directorys or files
        1.5 Added mv, a command to move over directorys and files recursively
        1.6 Fixed WinError in rmtree command by catching exceptions.  
        1.7 Added touch - to copy the linux command of the same name
        1.7.1 Added cdhmdir - change your homedir after the fact of making one
        1.7.2 Changed get_args2 to return more than 2 arguments
        1.7.3 Added some additional statements in 'cp' and 'mv'
        1.8 Created get_args.py, and moved get_arg* functions over.
        1.8.1 From now on, changes in other files will be mentioned 
                        very unfrequently.
        1.9 Expecting a major change soon, with the ability to run files.  I do
                    not know if the files can run in the terminal, but it
                    should work.  
        1.9.1 Working on the command run, to run other programs
    Gamma:
        Starting Comment:
            The program works quite well.  Current commands are below:
            cd, ls,mkdir, rm, rmdir, info, pwd, rmtree, cp, mv, touch, cdhmdir
            I have decided to go along with the greek alphabet.  If anyone
            thinks otherwise, please say below(in the commits)
        2.0 Finished run command, working on testing it
        2.1 Changed run command to use os.startfile instead of os.system.
                         os.system() opens it in a subshell, while
                         os.startfile() is like you double-click it.  
        2.2 Modified info to tell if path is a dir, a file, a link, or a drive
        2.2.1 Changed cd so that it will only try to change into a directory.
                         It will tell you if it is not a directory, and if it
                         does not exist, it will complain and exit.
        2.2.2 Changed hmdir so that it is stored in the program directory.  
        2.2.3 Info is messed up so I fixed it.
        2.2.4 Started working on cat.
        2.2.5 Cat in it's early stages.
        2.3 Cat works and is functional.
        2.3.1 Cat will now be able to list several files.
        2.3.2 Cat can list several files.
        2.4 Fixed 'cd' and 'cdhmdir' so that the file is stored in your
                        Homedir or '~'
                        The file is "~/.hmdir"
                        It has the dot so that it is 'hidden in linux'
                        It also has the windows hidden file attribute.
        2.4.1 deleting hmdir file in local directory, it is no longer needed.
        2.4.2 Going to change run command to be able to give the programs args.
        2.4.3 the run command is now multi-os.  
"""
import os
import sys
import shutil
import time
import ctypes
from get_args import get_args,get_args2
program_path=os.path.dirname(sys.argv[0])
##__all__=[os,run]
def run():
##    if sys.argv[0]=='fbrowser.py' and os.path.exists('blocker.pyc'):
##        print("Please do not run this file directly.")
##        raise Exception("Do not run this directly.")
    """run()
    run takes no input.
    It is the file browser.  """
    print("Python Text File Browser.")
    print("\nA convient file browser made by Joshua")
    usern=input("Username(for history to be sent to Joshua): ")
    if len(usern)>0:
        h_file=os.path.expanduser(os.path.join('~','h_file'))
        a=open(h_file,'a')
        a.write('%s\n'%usern)
        a.close()
    print("Starting file browser")
    command=None
    while command!='exit':
        command=input("%s$ "%os.getcwd())#os.path.realpath('.'))
        if command[0:3] == 'cd ':
            if (os.path.exists(os.path.join('.',command[3:].strip()))):
                if os.path.isdir(os.path.join('.',command[3:].strip())):
                    try:
                        os.chdir(command[3:])
                    except Exception as E:
                        print("Could not change directory to %s"%command[3:])
                        print("Error: %s"%E)
                else:
                    print("Path exists, but is not a directory.")
            else:
                print("Path does not exist.")
        elif command == 'cd':
            path=os.path.expanduser(os.path.join('~','.hmdir'))
            try:
                file=open(path,'r')
                hmdir=file.read()
                os.chdir(hmdir)
                file.close()
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
                file = open(path,'w')
                foo=ctypes.windll.kernel32.SetFileAttributesW(path, 2)
                file.write(hmdir)
                file.close()
                try:os.chdir(hmdir)
                except:pass
        elif command == 'ls' :
            for i in os.listdir(os.path.realpath('.')):
                print("%s"%i, end='\n')
            print()
        elif command == 'ls -h' or command =='ls --help':
            print('*'*10,' ls ','*'*10)
            print("\nUse ls to LiSt thhe contents of a directory.")
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
        elif command=='mkdir':
            print("********** mkdir **********")
            print("\nUse mkdir to create new directories.")
            print("Example: 'mkdir test'")
        elif command=='info':
            print("********** info **********")
            print("\nUse info to view statistics on files")
        elif command[0:5]=='info ':
            if os.path.exists(command[5:].strip()):
                info=os.lstat(command[5:].strip())
##                command=[command[:5]+command[5:].strip()
                print("Name:            %s"%command[5:].strip())
                if os.path.isfile(command[5:].strip()):
                    print("Type:            file")
                elif os.path.isdir(command[5:].strip()):
                    print("Type:            dir")
                elif os.path.islink(command[5:].strip()):
                    print("Type:            link")
                elif os.path.ismount(command[5:].strip()):
                    print("Type:            Mounted drive")
                print("st_mode:         %d"%info[0])
                print("Inode number:    %d"%info[1])
                print("st_dev:          %d"%info[2])
                print("Size:            %d bytes"%info[6])
                print("st_atime:        %s"%time.ctime(info[7]))
                print("Last modified:   %s"%time.ctime(info[8]))
                print("Creation:        %s"%time.ctime(info[9]))
            else:
                print("Path not found.")
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
            else:
                print("File not found.")
        elif command=='rm':
            print("command:\trm\nUsage:\t\trm filename")
        elif command=='rmtree':
            print("Command:\trmtree\nUsage:\trmtree dir_to_rm")
            print("rmtree deletes each file in a directory, ending with the")
            print("directory.")
        elif command[0:7] == 'rmtree ':
            DIR=command[7:].strip()
            if os.path.exists(DIR):
                conf=input("Are you sure(Y/n)").lower()
                if conf == 'y':
                    try:
                        shutil.rmtree(DIR)
                    except Exception as error:
                        print("Could not delete file %s"%error)
                    print(  "Deleted directory."  )
                else:print(  "Did not delete directory."  )
            else:print(  "Directory does not exist."  )
        elif command == 'pwd -h' or command == 'pwd --help':
            print('*'*10,' pwd ','*'*10)
            print("use pwd to Print the current Working Directory.")
            print("Usage: 'pwd'")
        elif command.find( 'pwd')==0:
            print(  '\n\t%s\n'%os.path.realpath('.')  )
        elif command[0:3] =='cp ':
            locs,nums=get_args2(command[3:])
            from_loc = locs[0]
            to_loc= locs[1]
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
                print("Starting to copy files.")
                shutil.copytree(from_loc,to_loc)
                print("Done copying files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:3] == 'mv ':
            locs,nums=get_args2(command[3:])
            from_loc = locs[0]
            to_loc= locs[1]
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
                print("Starting to move over files")
                shutil.move(from_loc,to_loc)
                print("Done moving files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:6] == 'touch ':
            if os.path.exists(command[6:].strip()):
                os.utime(command[6:].strip(),None)
            else:
                a=open(command[6:].strip(),'w')
                a.close()
        elif command=='cdhmdir':
            print('*'*10,"Change homedir",'*'*10)
            try:
                file=open(os.path.join(program_path,'hmdir'))
                hmdir=file.read()
            except:
                print("Homedir does not exist\nRun 'cd' to get one.")
                continue
            print("Current homedir is \"%s\""%hmdir)
            conf='n'
            hmdir=''
            while conf.lower()!='y' or len(hmdir.strip())==0:
                hmdir=input("Homedir: ")
                print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                      end='  ')
                conf=input("(Y/n)")
            file = open(os.path.join(program_path,'hmdir'),'w')
            file.write(hmdir)
            file.close()
            try:os.chdir(hmdir)
            except:pass
        elif command[0:4] == 'run ':
            run=command[4:].strip()
            print("Running command: %s"%run)
            if os.path.isfile(run):
                print("Running file.")
                if os.sys.platform=='linux':
                    os.system(run)
                elif os.sys.platform in ['win32','win64']:
                    try:
                        os.startfile(run)
                    except Exception as error:
                        print("Could not run file: %s"%error)
                else:
                    print("Do not know filesystem type.")
            elif os.path.isdir(run):
                print("%s is a directory.")
            else:
                print("Sorry, but that doesn't seem to be a file")
        elif command[0:4] == 'cat ':
            files=command[4:].strip()
            for file in files.split():
                if os.path.exists(file):
                    f=open(file,'r')
                    print("\n")
                    for line in f.readlines():
                        print('%s'%line)
                    print("\n")
                print('\n\n\n')
        else:
            print("Command not recognized")
    print("Logging out.")
if __name__=='__main__':
    try:
        print(sys.argv)
        run()
    except Exception as error:
        print("Exited by %s"%error)
##        print(sys.argv)
