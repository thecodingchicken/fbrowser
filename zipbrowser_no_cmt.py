import zipfile
import os
import time
try:
    import remove_comments
except ImportError:
    print("You don't have the remove_comments program")
    print("To get that, go to:")
    print("https://github.com/thecodingchicken/fbrowser")
    print("\nLook for the remove_comments.py program")
else:
    remove_comments.remove_cmts('zipbrowser.py')
    del remove_comments
def endswith(string,search):
    if search==string[0-(len(search)):]:
        return True
    return False
def verifyzip(name):
    if endswith(name,'.zip')==False:
        print("File does not end with .zip")
        print("Changing name...")
        return '{0}.zip'.format(name)
    else:
        return Name
    raise Exception("CAN'T GET HERE!!!")
def zipbrowser(filen):
    print('\n'*3)
    if os.path.exists(filen):
        path=os.path.abspath(filen)
        f_name=os.path.basename(path)
        print(path,f_name)
    else:
        print("File not found.")
    prompt=''
    while True:
        try:
            foo=input('{}> '.format(f_name))
        except:
            print("Enter exit to quit")
        else:
            if foo=='exit':
                print("Closing browser")
                break
            elif foo=='quit':
                print("Enter 'exit' to quit")
            elif foo[:5]=='open ':
                if os.path.exists(foo[5:].strip()):
                    print("File exists.")
                else:
                    print("Error:  file not found.")
                    continue
                if (endswith(foo[5:].strip(),'.zip')==True):
                    print("File ends with .zip")
                else:
                    print("File does not fit the '*\\.zip' wildcard.")
                    continue
                path=os.path.abspath(foo[5:].strip())
                f_name=os.path.basename(path)
                print("Filename: {0}".format(path))
            elif foo=='open':
                print("Use 'open' to open a .zip file.  ")
                print("If it gets anything else, it will complain.")
                print("The full path is not needed, so you can do things that")
                print(" are in the current directory or related to that,")
                print("such as ../test.zip")
            elif foo[:4]=='new ':
                print("NEW ZIP FILE")
                name=foo[4:].strip()
                name=verifyzip(name)
                if os.path.exists(name):
                    print("File exists.")
                    print("Delete file {0}".format(os.path.abspath(name)))
                    print("before creating a new one.")
                    continue
                else:
                    print("Creating file")
                    try:
                        a=zipfile.ZipFile(name,'w',8)
                        a.close()
                    except:
                        print("Error creating file")
                        del a
                    path=os.path.abspath(name)
                    f_name=os.path.basename(path)
                    print("Created file")
        finally:
            print('\n\n')
