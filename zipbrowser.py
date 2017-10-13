import zipfile
import os
import time

def zipbrowser(filen):
    if os.path.exists(filen):
        path=os.path.abspath(filen)
        f_name=os.path.basename(path)
        print(path,f_name)
    else:
        print("File not found.")
    prompt=''
    while True:
        try:
            foo=input('zipbrowser-{}> '.format(f_name))
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
                path=os.path.abspath(foo[5:].strip())
                f_name=os.path.basename(path)
                print("Filename: {0}".format(path))
            elif foo=='open':
                print("Use 'open' to open a .zip file.  ")
                print("If it gets anything else, it will complain.")
                print("The full path is not needed, so you can do things that")
                print(" are in the current directory or related to that,")
                print("such as ../test.zip")
                
        finally:
            print('\n\n')
