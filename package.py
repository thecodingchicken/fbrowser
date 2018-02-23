import base64,os
write_to="setup.py"
directory=[]
files=[]
for root,dirs,Files in os.walk('.'):
    d=dirs+Files
    for i in range(len(d)):
        if os.path.isdir(os.path.join(root,d[i])):
            directory.append(os.path.join(root,d[i]))
        elif os.path.isfile(os.path.join(root,d[i])):
            if root=='.' and d[i].count('setup.py')==1:continue
            elif root==os.path.join('.','build','lib'):continue
            elif os.path.join(root,d[i]).endswith('.pyc'):continue
            elif os.path.join(root,d[i]).endswith('.exe'):continue
            elif d[i].endswith('.zip'):continue
            elif '.git' in os.path.join(root,d[i]):
                continue
            if os.path.realpath(os.path.join(root,d[i]))==os.sys.argv[0]:
                continue
            files.append(os.path.join(root,d[i]))
del root,dirs,Files,d,i
files_text=[]
print("%-30s %10s %s"%("Name",'unencoded','encoded'))
for file in files:
    foo=open(file,'rb').read()
    foo2=base64.b85encode(foo)
    files_text.append(foo2)
    print("%-30s %10dB %dB"%(os.path.basename(file),len(foo),len(foo2)))
to_write="""import base64
import os
os.sys.stdout.write("Installing in current directory")
for DIR in %s:
    if os.path.exists(DIR):
        pass
    else:os.mkdir(DIR);os.sys.stdout.write("Made dir %%s\\n"%%DIR)
files=%s
files_text=%s
for i in range(len(files)):
    with open(files[i],'wb') as file:
        file.write(base64.b85decode(files_text[i]))
    os.sys.stdout.write("File %%s written\\n"%%os.path.realpath(files[i]))
os.sys.stdout.write("Done\\n\\n")
os.sys.stdout.write("Use \\"python3 fbrowser.py\\" to run")
"""%(directory,files,files_text)
with open(write_to,'wb') as write_file:
    a=write_file.write(to_write.encode())
    print("Size: %d bytes"%a)
print("Done!")
