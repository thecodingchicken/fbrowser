import os
import tarfile
class optionlist:
    """I couldn't think of a better name for this class.
    It is made to hold three objects, a number and two strings.
    The purpose of it is to use like a dict and a list.
    You display the number and the first string to the user,
    but the second is for the computer.
    """
    def __init__(self,number,public,private):
        """__init__(number,public,private
                     int   string string
        """  
        self._number=number
        self._public=public
        self._private=private
    def print_public(self,middle):
        """This function prints the public stuff about it.
           middle is formatting
           example:
               >>>a=optionlist(1,'Open tar archive','open'
               >>>a.print_public(':\\t')
               1:    Open tar archive
"""
        print("\t%s%s%s"%(self._number,middle,self._public))
def tarbrowser(filen=r'C:\Users\Joshua\Desktop\compressed files\Gutenberg.tar'):
    choice=-1
    choices=[optionlist(1, 'Open tar archive',  'open'  ),
             optionlist(2 ,'List tar archive',  'list'  ),
             optionlist(3 ,'Close tar archive', 'close' ),
             optionlist(4 ,'Quit',              'exit'  )
                        ]
    if os.path.exists(filen):
        print("File exists")
        filen=os.path.realpath(filen)
        basefilename=os.path.basename(filen)
        
    while True:#This loop exits when you enter the number that
        #means quit
        try:
            for i in range(len(choices)):
                choices[i].print_public(':\t')
            choice=int(input("Choice: "))
        except KeyboardInterrupt:
            print("^C found.  Enter the cooresponding number to exit")
            continue
        except ValueError:
            print("Enter a number")
            continue
        except Exception as e:
            print("Something went wrong.\nStack trace is '%s'"%e)
        else:
            print("Processing input")
            if choice<1:# choice is something, like -1
                print("Enter a number in the range 1-%d"%len(choices))
            elif choice>len(choices):
                print("Enter a number in the range 1-%d"%len(choices))
            else:
                if choice == 1:
                    filen='hi'
                    while ((not os.path.exists(filen)) or 
                           (not (filen[-4:]=='.tar'))):
                            filen=input("File:  ")
                            if (not os.path.exists(filen)):
                                print("File not found")
                                print("Other files in the folder")
                                try:
                                    d=os.listdir(os.path.dirname(filen))
                                except:
                                    print("Folder not found,using '.'")
                                    d=os.path.realpath('.')
                                    d=os.listdir(d)
                                for i in range(len(d)):
                                    print("%3d:\t %50s"%(i,d[i]))
                                print()

                               
                            elif(not (filen[-4:]=='.tar')):
                                print("File does not end in .tar")
                                
                elif choice==2:
                    print("This function is not working as of right now")
                    continue
                    #If you put code on the same indentation level after
                    #the continue, it doesn't go to it
                    #it is like
                    #goto b;
                    #printf("You can't see me!");
                    #b:
                if 1:
                    print("Listing archive")
                    print("Press 'd' to stop")
                    a=tarfile.TarFile(filen)
                    t=''
                    while
                elif choice==3:
                    print("You can enter '4' to exit anytime")
                elif choice==4:
                    print("Are you sure?(Y/n)",end=' ')
                    try:c=input().lower()
                    except:c='n'
                    if c[0]=='y':
                        print("Exiting")
                        break
                    else:
                        print("Canceled")
##tarbrowser()
