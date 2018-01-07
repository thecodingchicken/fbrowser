import os,time,remove_comments
remove_comments.remove_cmts('find_file_path.py')
def find_file(to_find,debug=False):
    valid=[]
    path=os.get_exec_path()
    for DIR_ in path:
        DIR=os.path.expandvars(DIR_)
        DIR=os.path.expanduser(DIR)
        try:
            for FILE in os.listdir(DIR):
                file=os.path.join(DIR,FILE)
                if to_find in file:
                    if debug: print("Found %s in %s"%(to_find,file))
                    valid.append(file)
        except FileNotFoundError:
            if DIR.strip()=='':continue
            if debug: print("Error, dir %s not found"%DIR)
        except Exception as e:
            if debug: print("***Error %s found."%e)
            break
    return valid
def get_valid_drives():
    valid=[]
    for drive_n in range(ord('A'),ord('Z')+1):
        d=chr(drive_n)
        try:n=os.listdir('%s:'%d)
        except:continue
        valid.append(chr(drive_n))
    return valid
def linux_path(win_path,debug=True):
    if debug:print("[ Start ] %s"%win_path)
    valid_drives=get_valid_drives()
    root='/'
    if win_path[:2].lower() not in ["%s:"%c.lower() for c in valid_drives]:
        raise Exception("How did you get here?!")
    win_path=win_path.replace('\\','/')
    win_path=win_path.replace(':','',1)
    win_path=win_path[0].lower()+win_path[1:]
    final="/%s"%(win_path)
    if debug:print("[ Final ] %s"%final)
    return final

if __name__=='__main__':
    get_valid_drives()
