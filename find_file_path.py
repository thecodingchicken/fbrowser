import os,time
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
