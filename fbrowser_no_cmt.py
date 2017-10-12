import os    
import shutil  
import time    
import ctypes
from get_args import get_args,get_args2
h_dir=os.path.expanduser('~') 
prmtusrnme=False
import remove_comments
from other_functions import string_contains
import tarfile
def run():
    print("Python Text File Browser.")
    print("\nA convient file browser made by Joshua")
    usern=''
    if prmtusrnme==True:
        usern=input("Username(for history to be sent to Joshua): ")
    if len(usern)>0 and prmtusrnme==True:
        h_file=os.path.join(h_dir,'h_file')
        a=open(h_file,'a')
        a.write('%s\n'%usern)
        a.close()
    print("Starting file browser")
    command=None
    while command!='exit':
        command=input("%s$ "%os.getcwd())
        if command[0:3] == 'cd ': 
            if (os.path.exists(os.path.join('.',command[3:].strip()))):
                if os.path.isdir(os.path.join('.',command[3:].strip())):
                    try:
                        os.chdir(command[3:].strip())
                    except Exception as E:
                        print("Could not change directory to %s"%command[3:])
                        print("Error: %s"%E)
                else:
                    print("Path exists, but is not a directory.")
            else:
                print("Path does not exist.")
        elif command == 'cd':
            path=os.path.expanduser(os.path.join('~','.hmdir'))
            print(path)
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
                    conf=input("(Y/n)")[0]
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
            except Exception as error:
                print("Error: could not create directory")
                print(error)
        elif command[0:4]=='tar ':
            if os.path.exists(command[4:].strip()):
                print("Tar file exists.  \nDepending on the size of the file,",
                      end='')
                print(" it may take a long time")
                file_n=command[4:].strip()
                print("Loaded tar file.  Starting tarbrowser.\n")
                text=''
                while True:
                    try:
                        text=input('%s >'%os.path.basename(file_n))
                    except:
                        print("To quit, type 'exit'")
                        continue
                    if text=='exit':
                        print("Exiting") 
                        break
                    elif text[:4]=='add ':
                        if os.path.exists(text[4:].strip()):
                            file=tarfile.TarFile(file_n,'a')
                            print("Opened tar archive.")
                            if os.path.isfile(text[4:].strip()):
                                print("Adding file to archive")
                                file.add(os.path.basename(text[4:].strip()))
                                os.unlink(os.path.basename(text[4:].strip()))
                            file.add(text[4:].strip())
                            print("Wrote file/folder")
                            file.close()
                        else:
                            print("File doesn't exist")
                    elif text=='view':
                        file=tarfile.TarFile(file_n)
                        c=file.next();
                        counter=0
                        while c!=None:
                            print(c)
                            c=file.next()
                            counter+=1;
                            if counter==9:
                                counter=0
                                try:foo=input('Press enter to continue')
                                except:
                                    print("Exiting.")
                                    break
                        file.close()
                file.close()
                del file
            else:
                print("Tar file not found.")
                print("Other tar files are:")
                files=os.listdir('.')
                for i in range(len(files)):
                    if string_contains(files[i],'.tar'):
                        print(files[i])
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
                    DIR=os.path.realpath(DIR)
                    os.chdir(DIR)
                    contents=os.listdir('.')
                    if len(contents) == 0:
                        os.chdir('..')
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
                    if os.path.isfile(command[3:].strip()):
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
                    else:
                        print(  "Deleted directory."  )
                else:
                    print(  "Did not delete directory."  )
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
                if os.path.isdir(from_loc):
                    shutil.copytree(from_loc,to_loc)
                elif os.path.isfile(from_loc):
                    shutil.copy(from_loc,to_loc)
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
                file=open(os.path.join(h_dir,'.hmdir'))
                hmdir=file.read()
                file.close()
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
            p=os.path.join(h_dir,'.hmdir')
            file = open(p,'w')
            file.write(hmdir)
            file.close()
            foo=ctypes.windll.kernel32.SetFileAttributesW(p, 2)
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
                    print("ANYONE WHO HAS THIS, PLEASE REPORT YOUR FILESYSTEM")
                    print("TYPE TO JOSHUA BOWE ON GITHUB.  ")
                    print("Report the words in double-quotes")
                    print("\n\t\"%s\"\t\n"%os.sys.platform)
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
        elif command[0:3]=='dir':
            print("What do you think that this is?\n\n\tWindows?\n\tNope.\n")
        else:
            print("Command not recognized")
    print("Logging out.")
if __name__=='__main__':
    try:
        run()
        1+2
    except Exception as error:
        print("Exited by %s"%error)
