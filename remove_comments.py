"""remove_comments.py

This file removes comments from a file.
It's only point is to make the file smaller.  It will save it in
FILENAME_no_cmt.FILENAMEEXT"""
def single_lines(l):
    for i in range(len(l)):
        if l[i].count('#')>=1:
            l[i]=l[i][:l[i].find('#')]
            l[i]+='\n'
            if l[i].strip()=='':l[i]=''
    return l[:]
def multi_lines(l):
    depth_p=0
    depth_b=0
    l2=[]
    in_cmt=False
    for i in range(len(l)):
        if l[i].count('"'+'""')==True:
            in_cmt=not in_cmt
            continue
        if in_cmt==False:
            l2.append(l[i])
    return l2
import os
def multi_lines2(l):
    depth_p=0
    depth_b=0
    depth_c=0
    in_quotes=None
    l2=[]
    in_cmt=False
    for line in range(len(l)):
        for char in l[line]:
            if char==chr(123):depth_p+=1
            elif char==chr(91):depth_b+=1
            elif char==chr(40):depth_c+=1
            elif char==chr(125):depth_p-=1
            elif char==chr(93):depth_b-=1
            elif char==chr(41):depth_c-=1
    print()
            
def remove_cmts(file):
    ##file='remove_comments.py'
    f,ext=os.path.splitext(file)
    try:
        a=open(file)#a is a referance to file
    except:
        print("The source file \"%s\" doesn't exist"%file)
        os.sys.exit(1)
    print("**********DECOMMENTING PROGRAM**********")
    print("Loading lines from file: %s"%file)
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
    lines=single_lines(lines[:])[:]
    lines=multi_lines(lines[:])[:]
    new_file='%s_no_cmt%s'%(f,ext)
    if True:
        print("Creating file")
        n=open(new_file,'w')
        for i in range(len(lines)):
            if lines[i]=='':continue
            n.write(lines[i])
        n.close()
        del a,n
        print("Finished writing to file.")
