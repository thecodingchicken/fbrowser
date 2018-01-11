"""This file contains the functions needed by all of the
other files.  fbrowser.py will not work without this code!
THis was transfered over at version 2.7.6

Future stuff to do:
        ##ls2--this command will someday be able to replace ls.
        ##it currently doesn't work.
##        elif command[0:4] == 'ls2 ':
##            args,string = get_args(command[3:])
##            if os.path.exists(string):
##                dir_listings = os.listdir(string)
##                for i in range(len(dir_listing)):
##                    to_print = '%s\t'%dir_listing[i]
##                    if 'l' in args:
##                        to_print = "%s\t"
"""
import os
import ctypes
import time
import shutil
from get_args import get_args2
import find_file_path
def string_contains(string, string2):
    "this checks to see if string2 is in string"
    i = 0-len(string2)
    if string[i:] == string2:
        return True
    return False

def get_input():
    """this function gets the input for the command line"""
    resp = input("%s$ "%os.getcwd().replace('\\', '/'))
    return resp

def command_cd(command):
    """command_cd(string)
    This function takes in a string and processes it"""
    #us to go.
    if os.path.exists(os.path.join('.', command[3:].strip())):
        #verify that the path exists.
        if os.path.isdir(os.path.join('.', command[3:].strip())):
            #verify that it is a directory.
            try:#put this in a try statement b/c file operations are
                #always weird.
                os.chdir(command[3:].strip())##cd to that dir,
                #stripping away all white space ex 'cd    hello' to
                #'hello'
            except PermissionError:
                print("Could not change directory to %s"%command[3:])
                print("You don't have the required permissions.")
            except FileNotFoundError:##oops..
                print("Could not change directory to %s"%command[3:])
                print("The directory doesn't exist.  ")
            except OSError:
                print("Could not change directory to %s"%command[3:])
        else:#Hey! It exists, but you didn't give me a directory
            print("Path exists, but is not a directory.")
    else:#What??? It doesn't exist.
        print("Path does not exist.")
    return

def command_cd_home(hm_dir):
    """Try to change to your homedir.  It trys to open a file in the
    given dir and cd to that dir, but if it fails, it asks you for one
    and saves it, then chdiring there.  """
    try:
        os.chdir(open(hm_dir, 'r').read())
    except (FileNotFoundError, PermissionError,
            OSError, IOError):#No homedir :-(
        print("No homedir given.")
        print("Please give a homir.")
        conf = 'n'
        hmdir = ''
        while conf.lower() != 'y' or not hmdir.strip():
            #While you haven't said yes to conf or
            #the hmdir input is nothing, TRY AGAIN.
            hmdir = input("Homedir: ")
            print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                  end='  ')
            conf = input("(Y/n)")[0]
        hmdir_file = open(hm_dir, 'w')#Open the file, write only.
        ctypes.windll.kernel32.SetFileAttributesW(hm_dir, 2)
        ##the line above uses ctypes to make the file hidden
        hmdir_file.write(hmdir)#write the homedir
        hmdir_file.close()#close the file
        try:
            os.chdir(hmdir)#Try to change to the directory
        except (FileNotFoundError,
                OSError, PermissionError) as error:
            print("Error:  Couldn't change directory to ")
            print("%s because of %s"%(hmdir, error))

def command_bank():
    "This is for the bank file, but it doesn't want to work at the moment"
    print("Sorry, but it isn't working")
    # try:
    #     import bank
    # except:
    #     print("Sorry, but it isn't working")
    # else:
    #     pass
def command_ls(command):
    """This funcion provides parsing and general working of the ls
    command, taking work away from the main file.  """
    if command == 'ls':# The user wants to list the current working
        #directory.
        for i in os.listdir(os.path.realpath('.')):#Use a for loop to
            print("%s"%i, end='\n')#list each object in the directory
        print()#Print a newline so that there is a seperation
    elif command == 'ls -h' or command == 'ls --help':#print help on
        print('*'*10, ' ls ', '*'*10)#ls
        print("\nUse ls to LiSt thhe contents of a directory.")
        print()
    elif command[0:3] == 'ls ':#we want to list something else.
        # args,string=get_args(command[3:])#this is for the future
        if command[3:] == '':##I have no idea why I put this here, but
            for i in os.listdir(os.path.realpath('.')):#if somehow you
                print("%s"%i, end='\n')#have text like 'ls ', which is
                #impossible because input strips away any whitespace
        elif os.path.exists(command[3:].strip()):#If it exists
            try:
                for i in os.listdir(command[3:].strip()):
                    print("%s"%i, end='\n')##list the directory wanted
                print()
            except (PermissionError, OSError, IOError):
                pass
        else:
            print("Path \"%s\" not found.  "%command[3:])#PATH NOT FOUND

def command_mkdir(command):
    """Change your dir to command with error checking"""
    try:
        os.mkdir(command.strip())##Try to create a directory
        print("Created dir: \"%s\""%command.strip())##Tell the
        #user that it was created
    except (PermissionError, FileExistsError,
            OSError, IOError) as error:
        print("Error: could not create directory")##It couldn't be
        print(error)##created, so let's tell them again.

def command_mkdir_help():
    "print the help on mkdir"
    print("********** mkdir **********")##  Help on mkdir
    print("\nUse mkdir to create new directories.")
    print("Example: 'mkdir test'")
    return

def command_info(command):
    "Parse, and print the response for the command that starts with info"
    if command == 'info':
        print("********** info **********")##help on info
        print("\nUse info to view statistics on files")
    elif command[0:5] == 'info ':##view the info on a filesys object
        if os.path.exists(command[5:].strip()):#verify that it exists
            info = os.lstat(command[5:].strip())##use os.lstat to get the
            #information about the file, practically everything
            #that you would ever need but the contents of the file.
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
            print("Inode number:    %d"%info[1])
            #print inode number
            print("st_dev:          %d"%info[2])
            print("Size:            %d bytes"%info[6])
            #print the size in bytes
            print("st_atime:        %s"%time.ctime(info[7]))
            #print the last access time
            print("Last modified:   %s"%time.ctime(info[8]))
            #print the past modification time
            print("Creation:        %s"%time.ctime(info[9]))
            #print the creation time
        else:#the path is not found
            print("Path not found.")

def command_rmdir(path_):
    """Try to delete the directory.   """
    # find the name of just the directory
    try:
        if os.path.exists(path_):#it exists, so let's do some tests
            path_ = os.path.realpath(path_)
            #um, let's do this so that
            #if the user does 'rmdir .' and it is blank, it will
            #cd .. and try to do that on the current directory,
            #which isn't empty
            os.chdir(path_)#cd to the dir
            info = os.listdir('.')#save the contents into a list
            if not info:#if it is empty, delete it
                os.chdir('..')
                os.rmdir(path_)##os.rmdir only works on empty dirs
                print("Deleted dir: %s"%path_)#print that it is deleted.
            else:#Sorry, but it contains stuff
                print("Directory is not empty.")
                os.chdir('..')
    except (PermissionError, FileNotFoundError,
            OSError, IOError) as error:##We had an error somewhere in there,
        print("Error: %s"%error)#so let's tell the user

def command_rm(path):
    "Try to delete a file with os.unlink"
    if os.path.exists(path):#
        try:
            if os.path.isfile(path):##A final check
                #to see if it is a file
                os.unlink(path)##use os.unlink to delete
                #the file(same as os.remove
            else:
                print("Error, path given isn't a file.  ")
        except PermissionError:#you tried to delete something that you
            print("Error: you cannot delete the file")#don't own...
            print("Not enough permissions")
    else:
        print("File not found.")
def command_rm_all(command):
    """Parse and execute text that starts with rm"""
    if command == 'rm':##help on rm
        print("command:\trm\nUsage:\t\trm filename")
    elif command == 'rmtree':
        print("Command:\trmtree\nUsage:\trmtree dir_to_rm")
        print("rmtree deletes each file in a directory, ending with the")
        print("directory.")
    elif command[0:3] == 'rm ':##The user wants to delete a file
        command_rm(command[3:].strip())
    elif command[0:6] == 'rmdir ':
        command_rmdir(command[6:].strip())
    elif command[0:7] == 'rmtree ':##the rmtree command.
        random_name = command[7:].strip()##get the directory.
        if os.path.exists(random_name):#check if it exists.
            conf = input("Are you sure(Y/n)").lower()#confirm... always a good
            if conf == 'y':#thing to do
                try:
                    shutil.rmtree(random_name)#try to delete it with shutil.rmtree
                except PermissionError as random_name:
                    ##we had an error, so tell the
                    print("Could not delete file %s"%random_name)
                    #user what it is
                else:#this worked.  The else statement executes this command
                    #if there was no problem.
                    print("Deleted directory.")
            else:##haha, they didn't want to do it.
                print("Did not delete directory.")
        else: print("Directory does not exist.")#self-explaining
    else:
        return False
    return True

def command_pwd(command):
    "Parse and print info for pwd"
    if command == 'pwd -h' or command == 'pwd --help':#help on pwd
        print('*'*10, ' pwd ', '*'*10)
        print("use pwd to Print the current Working Directory.")
        print("Usage: 'pwd'")
    elif command.find('pwd') == 0:#the user wants to find out the current dir
        print('\n\t%s\n'%os.path.realpath('.'))

def command_help(doc_):
    """Print the help for the string passed in."""
    print("Printing help on doc")
    info = doc_.split('\n')
    random_name = {'cnt':0, 'max_cnt':10,
                   'line':'', 'lines':[]}
    while info:
        random_name['line'] = info.pop(0)
        random_name['cnt'] += 1
        random_name['lines'].append('%s'%random_name['line'])
        if random_name['cnt'] == random_name['max_cnt']:
            print('\n'.join(random_name['lines']), end='')###List all in lines
            random_name['lines'] = []##Reset lines
            random_name['cnt'] = 0#reset count
            input("\n[ENTER]")
    del random_name, info
    return

def command_joshpad():
    "Try to start up joshpad"
    ##Joshpad, Joshua's
    try:#very own text editor.  THis is graphical.
        import text_editor#Import here, and
        text_editor.start()#start it up.
    except ImportError:
        print("Error: text editor file not found!")
        # The program wasn't in sys.path or .

def command_cp(command):
    """copy files"""
    # locs = get_args2(command[3:])[0]# For future stuff
    random_name = get_args2(command[3:])[0]
    random_name = {'from_loc':random_name[0],
                   'to_loc':random_name[1]}
    if (os.path.exists(random_name['from_loc']) and
            (not os.path.exists(random_name['to_loc']))):
        #the source has to exist and the destination can't exist.
        print("Starting to copy files.")# the shutil copy* stuff
        # gives no feedback.  I, someday, might try to do that.
        if os.path.isdir(random_name['from_loc']):##If it is a dir,
            shutil.copytree(random_name['from_loc'],
                            random_name['to_loc'],
                            list_f=True)
            # use copytree
        elif os.path.isfile(random_name['from_loc']):
        # if it is a file
            shutil.copy(random_name['from_loc'],
                        random_name['to_loc'],
                        list_f=True)
            # use just plain old copy
        print("Done copying files.")
    else:
        print("Source doesn't exist or the destination exists.")

def command_mv(command):
    """move files"""
    locs = get_args2(command[3:])[0]
    from_loc = locs[0]
    to_loc = locs[1]
    if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
        print("Starting to move over files")
        shutil.move(from_loc, to_loc)#move works on both dirs and
        #files
        print("Done moving files.")
    else:
        print("Source doesn't exist or the destination exists.")

def command_touch(path):
    """make a file if it doesn't exists, otherwise, update the timestamp."""
    #timestamp
    if os.path.exists(path.strip()):#if it exists,
        os.utime(path.strip(), None)#update the timestamp
    else:
        file = open(path.strip(), 'w')#create the file
        file.close()#close the file

def command_cdhmdir(h_dir):
    "change your set homedir"
    print('*'*10, "Change homedir", '*'*10)
    try:#put this in a try statement
##                print(h_dir)
        hmdir = open(os.path.join(h_dir, '.hmdir')).read()
    except (FileNotFoundError, PermissionError,
            OSError, PermissionError):
        print("Homedir does not exist\nRun 'cd' to get one.")#if this is
        #your first time, you have to do 'cd' to get one
        # I have no idea why I did this that way.
    print("Current homedir is \"%s\""%hmdir)#You have a homedir, so
    conf = 'n'
    hmdir = ''
    while conf.lower() != 'y' or not hmdir.strip():
        hmdir = input("Homedir: ")
        print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
              end='  ')
        conf = input("(Y/n)")
    p_spam = os.path.join(h_dir, '.hmdir')#get the path
    file = open(p_spam, 'w')#open it, write only, recreating it
    file.write(hmdir)#write the hmdir string
    file.close()#close the file
    ctypes.windll.kernel32.SetFileAttributesW(p_spam, 2)#set it invisible
    try:
        os.chdir(hmdir)#try to cd to that directory
    except (FileNotFoundError, PermissionError,
            OSError, PermissionError):
        print("Error, couldn't change dir")

def get_run_func():
    "return the function used per platform"
    if os.sys.platform == 'linux':#if you use linux
        #you don't have os.startfile.  os.system works just as well
        return os.system
    elif os.sys.platform in ['win32', 'win64']:#I don't think win64
        #is a platform.  I am on a 64-bit windows machine, and
        #python says that it is 'win32'.  I think that that is how
        #windows and python work.
        #try to use os.startfile.  If you use os.system,
        #and you are not in a command line, which this is
        #meant for(I only test it out in a command line), it
        #starts up a subshell and stays there.
        #os.startfile is a double-click
        return os.startfile
    elif os.sys.platform not in ['win32', 'win64', 'linux']:
        print("Do not know filesystem type.")#Unknown file type.
        print("ANYONE WHO HAS THIS, PLEASE REPORT YOUR FILESYSTEM")
        print("TYPE TO JOSHUA BOWE ON GITHUB.  ")
        print("Report the words in double-quotes")
        print("\n\t\"%s\"\t\n"%os.sys.platform)
        return os.system
    else:
        raise Exception()
def command_run(command):
    "try to run the file"
    #the file has to be a whole path, such as fbrowser3.5-install.exe
    #commands can not be used unless they are in the current directory
    #that will hopefully work someday.  But not with windows.  I will
    #have to find out a way to pipe the commands to the terminal before
    #that can work.
    random_name = command[4:].strip()#get the file
    print("Running command: %s"%random_name)
    if os.path.isfile(random_name):#if it is a file, run it
        print("Running file.")
        try:
            get_run_func()(random_name)
        except FileNotFoundError:
            print("Error, file not found")
        except PermissionError:
            print("Error, bad permissions")
    elif os.path.isdir(random_name):# it is a directory, so complain
        print("%s is a directory.")
    else: # it is not a file or directory
        print("\n\n*****Sorry, but that doesn't seem to be a file")
        print("Would you like to execute this in the command line?")
        print("It might leave a command prompt window behind")
        print("while it is running. If your program is graphical, ")
        print("you can close this.  Clearly, if it is not, then")
        print("DON'T!")
        print("\n\n")
        print("Valid locations of your file are below.")
        print("The top one will run first.")
        valid = find_file_path.find_file(random_name)
        if not valid:
            print("No file found")
        else:
            for valid_i in enumerate(valid):
                print("%-3d) %s"%(valid_i[0]+1, valid_i[1]))
        try:
            conf = input("(Y/n)")[0].lower()
        except (EOFError, KeyError):
            print("Sorry, but you gave an invalid input, ")
            print("Going back")
            return
        else:
            if conf == 'y':
                random_name = os.system(random_name)
                print("Ran.  Program gave return code %s"%(
                    random_name))
            else:
                print("Canceled.")
        del conf
        return

def command_cat(files):
    "list each file in files"
    for file in files.split():
        if os.path.exists(file):#if it exists
            print("\n")#print a newline
            print(''.join(open(file).readlines()))
            print("\n")#have another newline
        print('\n\n')

def command_clear():
    """clear the screen, changing for the operating system"""
    if os.sys.platform == 'win32':
        os.system('cls')
    elif os.sys.platform in ['linux', 'linux2', 'linux3',
                             'cygwin', 'darwin', 'os2', 'os2emx',
                             'freebsd7', 'freebsd8', 'freebsdN']:
        os.system('clear')
    else:
        os.system('clear|grep thisstringwillneverbeseen')
        os.system('cls|grep thisstringwillneverbeseen')

def print_start_info():
    "print the start info for the file browser"
    print("Python Text File Browser.")#intro
    print("\nA convient file browser made by Joshua")#intro
    print("Starting file browser")#When I first did this, it said
    #  "Starting browser".  I couldn't figure out why.  ;-)
    return None
