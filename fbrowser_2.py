#fbrowser.py
#!/bin/bash python3
#fbrowser.py
"""
Python text file browser
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
    tar        v2.6
    clear      v2.6.1
##    bank       v2.6.2
    text edit  v2.6.4
    joshpad    v2.7
    help       v2.7.3
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
        2.5.2 Added remove_comments-it will strip all single-line comments and
                         multi-line comments.  This makes the file shorter
        2.5.3 RFC tarfiles  -- I will make this able to read tarfiles.
        2.6.0 Tar-- this command will allow you to view .tar files.
        2.6.1 clear-clear the screen
        2.6.2 Added a bank command, so you can do checking from the command line
        2.6.3 Bank command is not working, taking off for now.
        2.7   Added a graphical text editor.
        2.7.1 joshpad - the graphical text editor now works by importing
                        the module and doing module_name.start()
        2.7.2 The fix to the sub-command run is here!  We can now
                        choose to execute things in the command shell in windows
                        A better way to verify this would be to also check the
                        path.  We could recursively search through each directory
                        if the file is in it.  We would stop at the first, and tell
                        the user which we are doing.  But, that isn't yet.
        2.7.3 Added help command- this lists the docs for this program.
                        it may use a program that will go over the
                        file and take it out.
        2.7.4 Fixed rmdir -- if the directory wasn't empty, it would stay in
                      the dir
        2.7.5 Removed threes command
        2.7.6 made code pep8 compliant(mostly) code is at 9.84/10
        v
"""
import os    #os module is needed for changing directory, creating files, ...
#Anything from sys can be accessed in os.sys
##b=shutil.tarfile.TarFile(os.path.realpath("..\..\..\Desktop\\compressed files\\Gutenberg.tar"))
import remove_comments
import other_functions_2 as other_f
H_DIR = os.path.expanduser('~') #h_dir is your homedir, where all global files
#are stored
HMDIR = os.path.expanduser(os.path.join('~', '.hmdir'))
remove_comments.remove_cmts('fbrowser.py')
CMD_NOT_FOUND = "Command not recognized."
def run():
    """
    run()
    run takes no input.
    It is the file browser.
    For more info, look at the __doc__ for this file, or for
    other_functions, also known as other_f
    """
    other_f.print_start_info()
    command = None
    #Set the command as None so that it doesn't complain
    while command != 'exit':#While loop(duh(it's in the name))
        command = other_f.get_input()
        #Print the current directory, and prompt for a command
        for option in ['tar', 'cp', 'touch', 'run',
                       'cat']:#These require one arg
            print(option, "uses one arg")
        for option in ['cd', 'ls', 'mkdir', 'info', 'rm',
                       'pwd', 'help']:#these require several args
            print(option, "uses more than one arg")
        for option in ['clear', 'joshpad', 'bank', 'dir']:
            print(option, "uses no args")
        if command == 'exit':
            pass
        elif command[0:5] == 'clear':
            other_f.command_clear()
        elif command == '':
            pass# Blank lines don't matter
        else:
            print(CMD_NOT_FOUND)
    print("Logging out.")
if __name__ == '__main__':
    try:
        run()##Run the program
    except Exception as error:
        print("Exited by %s"%error)
        raise
