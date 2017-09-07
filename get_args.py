def get_args(string):
    args=[]
    end=''
    possible = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I',
                'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a',
                'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
                'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                't', 'u', 'v', 'w', 'x', 'y', 'z']
    ready=False
    for i in range(1,len(string)):
        if string[i]== '-' and string[i-1]== ' ':
            end+=' '
            ready=True
            continue
        if ready==True:
            if string[i] in possible:
                args.append(string[i])
                
            else:
                end+=string[i]
                ready=False
            
    return args,end
def get_args2(s):
    if s.find('"')!=-1 or s.find("'")!=-1:
        pass
    else:
        l=s.split()
        if len(l)==2:
            return l,2
        elif len(l) == 1:
##            print("array is of length 1; exiting")
            l.append(None)
            return l,2
        else:
##            print("l is longer than an array of len(2)")
            return l,len(l)
