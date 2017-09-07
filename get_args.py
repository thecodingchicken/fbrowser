"""
get_args.py
Author: Joshua Bowe
License: GNU GPL

get_args.py is a file in the program fbrowser.
    Versions:
        0.0 Copyed all get_arg* functions over from fbrowser.
        0.1 Added help on get_args()
        0.2 Added help on get_args2()
"""
def get_args(string):
    """get_args(string)
    input: type==str
    output: args(list), end(string)
    you give get_args a string such as "ls -alt exampledir"
    it will parse the string for a dash that is after a space( ' -')
    all args are returned in args.
    everything else is in end, which is a type str
    that returns ['a','l','t'], "ls exampledir""""
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
    """
    get_args2(s)
    input: s == type str
    output: list,int

    s is a string such as "hello world"
    it then returns s.split()
    if len(s.split()) == 1, then it append None to the list and returns
    l,1
    if len(s.split()) == 2, then it returns l,2
    if len(s.split()) >2, then it returns l,len(l)
    
    """
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
