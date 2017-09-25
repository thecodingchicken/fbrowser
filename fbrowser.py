#fbrowser.py
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
        2.4.4 changed cp command to be able to copy over files
        2.5 Commented the whole thing for a friend and anyone else who wants
                         to read it and understand.  The file grew from 15.1 KB
                         to now 23.6 KB.
        2.5.1 Added dir command- it justs prints a message
        
"""
import os    #os module is needed for changing directory, creating files, ...
#Anything from sys can be accessed in os.sys
import shutil  #shutil module is used in copying, moving, and deleting
               #directory trees
import time    #time is used for the printing of dates in any other format
#than in seconds
import ctypes#This module is used in hiding files on windows
from get_args import get_args,get_args2#get_args is the companion file. 
h_dir=os.path.expanduser('~') #h_dir is your homedir, where all global files
#are stored
prmtusrnme=False#For PRoMpTing of the USeR NaME
def run():
    """run()
    run takes no input.
    It is the file browser.  """
    print("Python Text File Browser.")#intro
    print("\nA convient file browser made by Joshua")#intro
    usern=''
    if prmtusrnme==True:
        usern=input("Username(for history to be sent to Joshua): ")#get a
    #username.  This is pointless and annoying.  It will not be active if
    # prmtusrnme is False
    if len(usern)>0 and prmtusrnme==True:#if the usern is not blank and
        #you are allowed to get the username
        h_file=os.path.join(h_dir,'h_file')#get the location of the file
        a=open(h_file,'a')#open the file in appending mode, creating if
        #needed
        a.write('%s\n'%usern)#write it in a *fancy* way
        a.close()#close the file
    print("Starting file browser")#When I first did this, it said
    #  "Starting browser".  I couldn't figure out why.  ;-)
    command=None#Set the command as None so that it doesn't
    #complain
    while command!='exit':#While loop(duh(it's in the name))
        command=input("%s$ "%os.getcwd())#Print the current directory,
        # and prompt for a command
        if command[0:3] == 'cd ': #command='cd', and they have somewhere for
            #us to go.
            if (os.path.exists(os.path.join('.',command[3:].strip()))):
                #verify that the path exists.
                if os.path.isdir(os.path.join('.',command[3:].strip())):
                    #verify that it is a directory.
                    try:#put this in a try statement b/c file operations are
                        #always weird.
                        os.chdir(command[3:].strip())##cd to that dir,
                        #stripping away all white space ex 'cd    hello' to
                        #'hello'
                    except Exception as E:##oops..
                        print("Could not change directory to %s"%command[3:])
                        #We can't change directory, so let's tell the user
                        print("Error: %s"%E)
                        #and the reason why.  I don't know any reason why this
                        #would happen
                else:#Hey! It exists, but you didn't give me a directory
                    print("Path exists, but is not a directory.")
            else:#What??? It doesn't exist.  
                print("Path does not exist.")
        elif command == 'cd':##The user wants to change to the home directory
            path=os.path.expanduser(os.path.join('~','.hmdir'))
            print(path)
            #path is to a file that contains the homedir.  The homedir does
            #not have to match real life, but it is better to have it that
            #way.
            try:
                file=open(path,'r')##Open the file, read only
                hmdir=file.read()##Read the first line.
                os.chdir(hmdir)#cd to that location
                file.close()##close the file, you might have problems later
                #if the file is still open.
            except:#No homedir :-(
                print("No homedir given.")
                print("Please give a homir.")
                conf='n'
                hmdir=''
                while conf.lower()!='y' or len(hmdir.strip())==0:
                    #While you haven't said yes to conf or
                    #the hmdir input is nothing, TRY AGAIN.
                    hmdir=input("Homedir: ")
                    print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                          end='  ')
                    conf=input("(Y/n)")[0]
                file = open(path,'w')#Open the file, write only.  
                foo=ctypes.windll.kernel32.SetFileAttributesW(path, 2)
                ##the line above uses ctypes to make the file hidden
                file.write(hmdir)#write the homedir
                file.close()#close the file
                try:os.chdir(hmdir)#Try to change to the directory
                except:pass##fail silently
        elif command == 'ls' :##The user wants to list the current working
            #directory.
            for i in os.listdir(os.path.realpath('.')):#Use a for loop to 
                print("%s"%i, end='\n')#list each object in the directory
            print()#Print a newline so that there is a seperation 
        elif command == 'ls -h' or command =='ls --help':#print help on
            print('*'*10,' ls ','*'*10)#ls
            print("\nUse ls to LiSt thhe contents of a directory.")
            print()
        elif command[0:3] == 'ls ':#we want to list something else.  
            args,string=get_args(command[3:])#this is for the future
            if os.path.exists(command[3:]):#If it exists
                startdir=os.path.realpath('.')#Use this to return here
                try:os.chdir(command[3:])#cd to that directory
                except Exception as E:#oops, so let's print it
                    print("Error: %s"%E)
                    continue
                for i in os.listdir(os.path.realpath('.')):
                    print("%s"%i, end='\n')##list the current dir
                    
                os.chdir(startdir)#cd back to where you were when you started
            elif command[3:]=='':##I have no idea why I put this here, but
                for i in os.listdir(os.path.realpath('.')):#if somehow you 
                    print("%s"%i, end='\n')#have text like 'ls ', which is
                    #impossible because input strips away any whitespace
                print()
            else:
                print("Path \"%s\" not found.  "%command[3:])#PATH NOT FOUND
        ##ls2--this command will someday be able to replace ls.
        ##it currently doesn't work.  
##        elif command[0:4]=='ls2 ':
##            args,string=get_args(command[3:])
##            if os.path.exists(string):
##                dir_listings=os.listdir(string)
##                for i in range(len(dir_listing)):
##                    to_print='%s\t'%dir_listing[i]
##                    if 'l' in args:
##                        to_print="%s\t"
        elif command[0:6] =='mkdir ':
            try:
                os.mkdir(command[6:].strip())##Try to create a directory
                print("Created dir: \"%s\""%command[6:].strip())##Tell the
                #user that it was created
            except Exception as error:
                print("Error: could not create directory")##It couldn't be 
                print(error)##created, so let's tell them again.
        elif command=='mkdir':
            print("********** mkdir **********")##  Help on mkdir
            print("\nUse mkdir to create new directories.")
            print("Example: 'mkdir test'")
        elif command=='info':
            print("********** info **********")##help on info
            print("\nUse info to view statistics on files")
        elif command[0:5]=='info ':##view the info on a filesys object
            if os.path.exists(command[5:].strip()):#verify that it exists
                info=os.lstat(command[5:].strip())##use os.lstat to get the
                #information about the file, practically everything
                #that you would ever need but the contents of the file.  
##                command=[command[:5]+command[5:].strip()
                print("Name:            %s"%command[5:].strip())##print name
                if os.path.isfile(command[5:].strip()):
                    print("Type:            file")##print that it is a file
                elif os.path.isdir(command[5:].strip()):
                    print("Type:            dir")##print that it is a dir
                elif os.path.islink(command[5:].strip()):
                    print("Type:            link")##print that it is a link
                elif os.path.ismount(command[5:].strip()):
                    print("Type:            Mounted drive")#print that it is
                    #a disk drive
                print("st_mode:         %d"%info[0])
                print("Inode number:    %d"%info[1])#print inode number
                print("st_dev:          %d"%info[2])
                print("Size:            %d bytes"%info[6])#print the size in
                #bytes
                print("st_atime:        %s"%time.ctime(info[7]))#print the
                #last access time
                print("Last modified:   %s"%time.ctime(info[8]))#print the
                #past modification time
                print("Creation:        %s"%time.ctime(info[9]))#print the
                #creation time
            else:#the path is not found
                print("Path not found.")
        elif command[0:6] == 'rmdir ':##delete an empty directory
            DIR=command[6:].strip()#find the name of just the directory
            try:
                if os.path.exists(DIR):#it exists, so let's do some tests
                    DIR=os.path.realpath(DIR)#um, let's do this so that
                    #if the user does 'rmdir .' and it is blank, it will
                    #cd .. and try to do that on the current directory,
                    #which isn't empty
                    os.chdir(DIR)#cd to the dir
                    contents=os.listdir('.')#save the contents into a list
                    if len(contents) == 0:#if it is empty, delete it
                        os.chdir('..')
                        os.rmdir(DIR)##os.rmdir only works on empty dirs
                        print("Deleted dir: %s"%DIR)#print that it is deleted.
                    else:#Sorry, but it contains stuff
                        print("Directory is not empty.")
            except Exception as error:##We had an error somewhere in there,
                print("Error: %s"%error)#so let's tell the user
        elif command.find( 'exit' ) != -1:#if the command is 'exit',
            #let's go evaluate the while statement again.  If we don't
            #pass on, it will say that the command is not found.
            #Since it is clearly a command, we have to have it in the
            #greatest if...elif...else statment in the program.
            pass
        elif command[0:3] == 'rm ':##The user wants to delete a file
            if os.path.exists(command[3:].strip()):#
                try:
                    if os.path.isfile(command[3:].strip()):##A final check
                        #to see if it is a file
                        os.unlink(command[3:].strip())##use os.unlink to delete
                        #the file(same as os.remove
                except PermissionError:#you tried to delete something that you
                    print("Error: you cannot delete the file")#don't own...
                    print("Not enough permissions")
            else:
                print("File not found.")
        elif command=='rm':##help on rm
            print("command:\trm\nUsage:\t\trm filename")
        elif command=='rmtree':#help on rmtree
            print("Command:\trmtree\nUsage:\trmtree dir_to_rm")
            print("rmtree deletes each file in a directory, ending with the")
            print("directory.")
        elif command[0:7] == 'rmtree ':##the rmtree command.  
            DIR=command[7:].strip()##get the directory.  
            if os.path.exists(DIR):#check if it exists.
                conf=input("Are you sure(Y/n)").lower()#confirm... always a good
                if conf == 'y':#thing to do
                    try:
                        shutil.rmtree(DIR)#try to delete it with shutil.rmtree
                    except Exception as error:##we had an error, so tell the 
                        print("Could not delete file %s"%error)#user what it
                        #is
                    else:#this worked.  The else statement executes this command
                        #if there was no problem.  
                        print(  "Deleted directory."  )
                else:##haha, they didn't want to do it.
                    print(  "Did not delete directory."  )
            else:print(  "Directory does not exist."  )#self-explaining
        elif command == 'pwd -h' or command == 'pwd --help':#help on pwd
            print('*'*10,' pwd ','*'*10)
            print("use pwd to Print the current Working Directory.")
            print("Usage: 'pwd'")
        elif command.find( 'pwd')==0:#the user wants to find out the current dir
            print(  '\n\t%s\n'%os.path.realpath('.')  )
        elif command[0:3] =='cp ':##CoPy something
            locs,nums=get_args2(command[3:])
            from_loc = locs[0]#get the from-location
            to_loc= locs[1]#get the to-location
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):#the
                #source has to exist and the destination can't exist.
                print("Starting to copy files.")##the shutil copy* stuff
                #gives no feedback.  I, someday, might try to do that.  
                if os.path.isdir(from_loc):##If it is a dir, 
                    shutil.copytree(from_loc,to_loc)#use copytree
                elif os.path.isfile(from_loc):#if it is a file
                    shutil.copy(from_loc,to_loc)#use just plain old copy
                print("Done copying files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:3] == 'mv ':#move files over
            locs,nums=get_args2(command[3:])
            from_loc = locs[0]
            to_loc= locs[1]
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
                print("Starting to move over files")
                shutil.move(from_loc,to_loc)#move works on both dirs and
                #files
                print("Done moving files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:6] == 'touch ':#create a blank file or update the
            #timestamp
            if os.path.exists(command[6:].strip()):#if it exists,
                os.utime(command[6:].strip(),None)#update the timestamp
            else:
                a=open(command[6:].strip(),'w')#create the file
                a.close()#close the file
        elif command=='cdhmdir':##change your homedir
            print('*'*10,"Change homedir",'*'*10)
            try:#put this in a try statement
##                print(h_dir)
                file=open(os.path.join(h_dir,'.hmdir'))#this is to check that 
                hmdir=file.read()#you already have a homedir
                file.close()#always close a file
            except:
                print("Homedir does not exist\nRun 'cd' to get one.")#if this is
                continue#your first time, you have to do 'cd' to get one
                # I have no idea why I did this that way.  
            print("Current homedir is \"%s\""%hmdir)#You have a homedir, so 
            conf='n'#let's tell them.  Set conf to 'n' and hmdir to ''
            hmdir=''#an empty string.
            while conf.lower()!='y' or len(hmdir.strip())==0:
                hmdir=input("Homedir: ")
                print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                      end='  ')
                conf=input("(Y/n)")
            p=os.path.join(h_dir,'.hmdir')#get the path
            file = open(p,'w')#open it, write only, recreating it
            file.write(hmdir)#write the hmdir string
            file.close()#close the file
            foo=ctypes.windll.kernel32.SetFileAttributesW(p, 2)#set it invisible
            try:os.chdir(hmdir)#try to cd to that directory
            except:pass#fail silently
        elif command[0:4] == 'run ':#the user wants to run a file
            #the file has to be a whole path, such as fbrowser3.5-install.exe
            #commands can not be used unless they are in the current directory
            #that will hopefully work someday.  But not with windows.  I will
            #have to find out a way to pipe the commands to the terminal before
            #that can work.
            run=command[4:].strip()#get the file
            print("Running command: %s"%run)
            if os.path.isfile(run):#if it is a file, run it
                print("Running file.")
                if os.sys.platform=='linux':#if you use linux
                    #you don't have os.startfile.  os.system works just as well
                    os.system(run)
                elif os.sys.platform in ['win32','win64']:#I don't think win64
                    #is a platform.  I am on a 64-bit windows machine, and
                    #python says that it is 'win32'.  I think that that is how
                    #windows and python work.
                    try:#try to use os.startfile.  If you use os.system,
                        #and you are not in a command line, which this is
                        #meant for(I only test it out in a command line), it
                        #starts up a subshell and stays there.
                        #os.startfile is a double-click
                        os.startfile(run)
                    except Exception as error:
                        print("Could not run file: %s"%error)
                else:
                    print("Do not know filesystem type.")#Unknown file type.
                    print("ANYONE WHO HAS THIS, PLEASE REPORT YOUR FILESYSTEM")
                    print("TYPE TO JOSHUA BOWE ON GITHUB.  ")
                    print("Report the words in double-quotes")
                    print("\n\t\"%s\"\t\n"%os.sys.platform)
            elif os.path.isdir(run):#it is a directory, so complain
                print("%s is a directory.")
            else:#it is not a file or directory
                print("Sorry, but that doesn't seem to be a file")
        elif command[0:4] == 'cat ':#list every file
            files=command[4:].strip()##seperate it so that you can do
            #several files
            for file in files.split():
                if os.path.exists(file):#if it exists
                    f=open(file,'r')#open read-only
                    print("\n")#print a newline
                    for line in f.readlines():
                        print('%s'%line)#print each line
                    print("\n")#have another newline
                print('\n\n\n')
        elif command[0:3]=='dir':
            print("What do you think that this is?\n\n\tWindows?\n\tNope.\n")
        else:
            print("Command not recognized")
    print("Logging out.")
if __name__=='__main__':
    try:
        print(os.sys.argv)
        run()
    except Exception as error:
        print("Exited by %s"%error)
##        print(sys.argv)
