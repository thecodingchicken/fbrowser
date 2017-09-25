"""remove_comments.py

This file removes comments from a file.
It's only point is to make the file smaller.  It will save it in
FILENAME_no_cmt.FILENAMEEXT"""
import os
file='fbrowser.py'
f,ext=os.path.splitext(file)
try:
    a=open(file)#a is a referance to file
except:
    print("The source file \"%s\" doesn't exist"%file)
    os.sys.exit(1)

print("Loading lines from file...")
print("This may take a long time.  Press ^C to exit if you don't want to.")
try:
    lines=a.readlines()
    a.close()
except KeyboardInterrupt:
    print("Exiting")
    a.close()
    os.sys.exit(1)
except EOFError:
    print("Exiting")
    a.close()
    os.sys.exit(1)
except Exception as E:
    a.close()
    print("Exception found:\n\t\t%s"%E)
    sys.exit(1)
print("Loaded file")

for i in range(len(lines)):
    if lines[i].count('#')>=1:
        lines[i]=lines[i][:lines[i].find('#')]
        lines[i]+='\n'
        if lines[i].strip()=='':lines[i]=''

new_file='%s_no_cmt%s'%(f,ext)
if True:# not os.path.exists(new_file):
    print("Creating file")
    n=open(new_file,'w')
    for i in range(len(lines)):
        if lines[i]=='':continue
        n.write(lines[i])
    n.close()
    del a,n
    print("Finished writing to file.")
