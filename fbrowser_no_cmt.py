import os    
import shutil  
import time    
import ctypes
from get_args import get_args2
import find_file_path
import remove_comments
import tarb
H_DIR = os.path.expanduser('~') 
remove_comments.remove_cmts('fbrowser.py')

def run():
    print("Python Text File Browser.")
    print("\nA convient file browser made by Joshua")
    print("Starting file browser")
    command = None
    while command != 'exit':
        current_dir = os.getcwd()
        command = input("%s$ "%current_dir.replace('\\', '/'))
        if command[0:3] == 'cd ': 
            if os.path.exists(os.path.join('.', command[3:].strip())):
                if os.path.isdir(os.path.join('.', command[3:].strip())):
                    try:
                        os.chdir(command[3:].strip())
                    except PermissionError:
                        print("Could not change directory to %s"%command[3:])
                        print("You don't have the required permissions.")
                    except FileNotFoundError:
                        print("Could not change directory to %s"%command[3:])
                        print("The directory doesn't exist.  ")
                    except OSError:
                        print("Could not change directory to %s"%command[3:])
                else:
                    print("Path exists, but is not a directory.")
            else:
                print("Path does not exist.")
        elif command == 'cd':
            path = os.path.expanduser(os.path.join('~', '.hmdir'))
            try:
                file = open(path, 'r')
                hmdir = file.read()
                os.chdir(hmdir)
                file.close()
            except (FileNotFoundError, PermissionError,
                    OSError, IOError):
                print("No homedir given.")
                print("Please give a homir.")
                conf = 'n'
                hmdir = ''
                while conf.lower() != 'y' or not hmdir.strip():
                    hmdir = input("Homedir: ")
                    print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                          end='  ')
                    conf = input("(Y/n)")[0]
                file = open(path, 'w')
                spam = ctypes.windll.kernel32.SetFileAttributesW(path, 2)
                del spam
                file.write(hmdir)
                file.close()
                try:
                    os.chdir(hmdir)
                except (FileNotFoundError,
                        OSError, PermissionError) as dir_error:
                    print("Error:  Couldn't change directory to ")
                    print("%s because of %s"%(hmdir, dir_error))
        elif command == 'bank':
            print("Sorry, but it isn't working")
        elif command == 'ls':
            for i in os.listdir(os.path.realpath('.')):
                print("%s"%i, end='\n')
            print()
        elif command == 'ls -h' or command == 'ls --help':
            print('*'*10, ' ls ', '*'*10)
            print("\nUse ls to LiSt thhe contents of a directory.")
            print()
        elif command[0:3] == 'ls ':
            if os.path.exists(command[3:]):
                startdir = os.path.realpath('.')
                try:
                    os.chdir(command[3:])
                except (FileNotFoundError, PermissionError,
                        OSError, IOError) as error:
                    print("Error: %s"%error)
                    continue
                for i in os.listdir(os.path.realpath('.')):
                    print("%s"%i, end='\n')
                os.chdir(startdir)
            elif command[3:] == '':
                for i in os.listdir(os.path.realpath('.')):
                    print("%s"%i, end='\n')
                print()
            else:
                print("Path \"%s\" not found.  "%command[3:])
        elif command[0:6] == 'mkdir ':
            try:
                os.mkdir(command[6:].strip())
                print("Created dir: \"%s\""%command[6:].strip())
            except (PermissionError, FileExistsError,
                    OSError, IOError) as error:
                print("Error: could not create directory")
                print(error)
        elif command[0:4] == 'tar ':
            tarb.tarb(command[4:])
        elif command == 'mkdir':
            print("********** mkdir **********")
            print("\nUse mkdir to create new directories.")
            print("Example: 'mkdir test'")
        elif command == 'info':
            print("********** info **********")
            print("\nUse info to view statistics on files")
        elif command[0:5] == 'info ':
            if os.path.exists(command[5:].strip()):
                info = os.lstat(command[5:].strip())
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
            dir_to_del = command[6:].strip()
            try:
                if os.path.exists(dir_to_del):
                    dir_to_del = os.path.realpath(dir_to_del)
                    os.chdir(dir_to_del)
                    contents = os.listdir('.')
                    if not contents:
                        os.chdir('..')
                        os.rmdir(dir_to_del)
                        print("Deleted dir: %s"%dir_to_del)
                    else:
                        print("Directory is not empty.")
                        os.chdir('..')
            except (PermissionError, FileNotFoundError,
                    OSError, IOError) as error:
                print("Error: %s"%error)
        elif command.find('exit') != -1:
            pass
        elif command[0:3] == 'rm ':
            if os.path.exists(command[3:].strip()):
                try:
                    if os.path.isfile(command[3:].strip()):
                        os.unlink(command[3:].strip())
                except PermissionError:
                    print("Error: you cannot delete the file")
                    print("Not enough permissions")
            else:
                print("File not found.")
        elif command == 'rm':
            print("command:\trm\nUsage:\t\trm filename")
        elif command == 'rmtree':
            print("Command:\trmtree\nUsage:\trmtree dir_to_rm")
            print("rmtree deletes each file in a directory, ending with the")
            print("directory.")
        elif command[0:7] == 'rmtree ':
            dir_to_del = command[7:].strip()
            if os.path.exists(dir_to_del):
                conf = input("Are you sure(Y/n)").lower()
                if conf == 'y':
                    try:
                        shutil.rmtree(dir_to_del)
                    except PermissionError as error:
                        print("Could not delete file %s"%error)
                    else:
                        print("Deleted directory.")
                else:
                    print("Did not delete directory.")
            else: print("Directory does not exist.")
        elif command == 'pwd -h' or command == 'pwd --help':
            print('*'*10, ' pwd ', '*'*10)
            print("use pwd to Print the current Working Directory.")
            print("Usage: 'pwd'")
        elif command.find('pwd') == 0:
            print('\n\t%s\n'%os.path.realpath('.'))
        elif command == 'help':
            print("Printing help on doc")
            main_doc = __doc__.split('\n')
            cnt = 0
            max_cnt = 10
            lines = []
            while main_doc:
                line = main_doc.pop(0)
                cnt += 1
                lines.append('%s'%line)
                if cnt == max_cnt:
                    print('\n'.join(lines), end='')
                    lines = []
                    cnt = 0
                    input("\n[ENTER]")
        elif command == 'help()':
            help()
        elif command[0:7] == 'help() ' and len(command) > 7:
            print("This doesn't work currently.")
        elif command == 'text editor' or command == 'joshpad':
            print("Sorry, but this isn't functional at the moment")
            if input("password") != 'helloworld':
                continue
            try:
                import text_editor
                text_editor.start()
            except:
                print("Done")
            else:
                pass
        elif command[0:3] == 'cp ':
            locs = get_args2(command[3:])[0]
            from_loc = locs[0]
            to_loc = locs[1]
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
                print("Starting to copy files.")
                if os.path.isdir(from_loc):
                    shutil.copytree(from_loc, to_loc, list_f=True)
                elif os.path.isfile(from_loc):
                    shutil.copy(from_loc, to_loc, list_f=True)
                print("Done copying files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:3] == 'mv ':
            locs = get_args2(command[3:])[0]
            from_loc = locs[0]
            to_loc = locs[1]
            if os.path.exists(from_loc) and (not os.path.exists(to_loc)):
                print("Starting to move over files")
                shutil.move(from_loc, to_loc)
                print("Done moving files.")
            else:
                print("Source doesn't exist or the destination exists.")
        elif command[0:6] == 'touch ':
            if os.path.exists(command[6:].strip()):
                os.utime(command[6:].strip(), None)
            else:
                tmp_f = open(command[6:].strip(), 'w')
                tmp_f.close()
        elif command == 'cdhmdir':
            print('*'*10, "Change homedir", '*'*10)
            try:
                file = open(os.path.join(H_DIR, '.hmdir'))
                hmdir = file.read()
                file.close()
            except:
                print("Homedir does not exist\nRun 'cd' to get one.")
                continue
            print("Current homedir is \"%s\""%hmdir)
            conf = 'n'
            hmdir = ''
            while conf.lower() != 'y' or not hmdir.strip():
                hmdir = input("Homedir: ")
                print("\n\nHomedir is \"%s\"\nIs that correct?"%hmdir,
                      end='  ')
                conf = input("(Y/n)")
            p_spam = os.path.join(H_DIR, '.hmdir')
            file = open(p_spam, 'w')
            del p_spam
            file.write(hmdir)
            file.close()
            spam = ctypes.windll.kernel32.SetFileAttributesW(p_spam, 2)
            try:
                os.chdir(hmdir)
            except:
                pass
        elif command[0:4] == 'run ':
            run_f = command[4:].strip()
            print("Running command: %s"%run_f)
            if os.path.isfile(run_f):
                print("Running file.")
                if os.sys.platform == 'linux':
                    os.system(run_f)
                elif os.sys.platform in ['win32', 'win64']:
                    try:
                        os.startfile(run_f)
                    except FileNotFoundError as error:
                        print("Could not run file: file not found"%error)
                else:
                    print("Do not know filesystem type.")
                    print("ANYONE WHO HAS THIS, PLEASE REPORT YOUR FILESYSTEM")
                    print("TYPE TO JOSHUA BOWE ON GITHUB.  ")
                    print("Report the words in double-quotes")
                    print("\n\t\"%s\"\t\n"%os.sys.platform)
            elif os.path.isdir(run_f):
                print("%s is a directory.")
            else: 
                print("\n\n*****Sorry, but that doesn't seem to be a file")
                print("Would you like to execute this in the command line?")
                print("It might leave a command prompt window behind")
                print("while it is running. If your program is graphical, ")
                print("you can close this.  Clearly, if it is not, then")
                print("DON'T!")
                print("\n\n")
                print("Valid locations of your file are below.")
                print("The top one will run first.")
                valid = find_file_path.find_file(run)
                if not valid:
                    print("No file found")
                else:
                    for valid_i in enumerate(valid):
                        print("%-3d) %s"%(valid_i[0]+1, valid_i[1]))
                try:
                    conf = input("(Y/n)")[0].lower()
                except:
                    print("Sorry, but you gave an invalid input, ")
                    print("Going back")
                    continue
                else:
                    if conf == 'y':
                        return_number = os.system(run_f)
                        print("Ran.  Program gave return code %s"%(
                            return_number))
                    else:
                        print("Canceled.")
                del conf
        elif command[0:4] == 'cat ':
            files = command[4:].strip()
            for file in files.split():
                if os.path.exists(file):
                    spam_file = open(file, 'r')
                    print("\n")
                    for line in spam_file.readlines():
                        print('%s'%line)
                    print("\n")
                    spam_file.close()
                print('\n\n\n')
        elif command[0:3] == 'dir':
            print("What do you think that this is?\n\n\tWindows?\n\tNope.\n")
        elif command[0:5] == 'clear':
            if os.sys.platform == 'win32':
                tmp = os.system('cls')
                del tmp
            elif os.sys.platform in ['linux', 'linux2', 'linux3',
                                     'cygwin', 'darwin', 'os2', 'os2emx',
                                     'freebsd7', 'freebsd8', 'freebsdN']:
                os.system('clear')
            else:
                try:
                    os.system('clear|grep thisstringwillneverbeseen')
                except:
                    try:
                        os.system('cls|grep thisstringwillneverbeseen')
                    except:
                        print("Sorry,but no known command clears the screen")
        elif command == '':
            pass
        else:
            print("Command not recognized")
    print("Logging out.")
if __name__ == '__main__':
    try:
        run()
    except Exception as error:
        print("Exited by %s"%error)
        raise
