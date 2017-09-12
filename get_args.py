"""
get_args.py
Author: Joshua Bowe
License: GNU GPL

get_args.py is a file in the program fbrowser.
    Versions:
        0.0 Copyed all get_arg* functions over from fbrowser.
        0.1 Added help on get_args()
        0.2 Added help on get_args2()
        0.3 Added find_amt, a function to find the total amounts of char in s
        0.4 Tried to change get_args2(), but it doth not work.  
"""
def get_args(string):
    """get_args(string)
    input: type==str
    output: args(list), end(string)
    you give get_args a string such as "ls -alt exampledir"
    it will parse the string for a dash that is after a space( ' -')
    all args are returned in args.
    everything else is in end, which is a type str
    that returns ['a','l','t'], "ls exampledir" """
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
def find_amt(s,char):
    total=0
    for i in s:
        if i==char:
            total+=1
    return total
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
    l=[]
    s2=s[:]
    while (s2.find('"')!=-1 or s2.find("'")!=-1) and len(s2)!=0:
        if s2.find('"')==0:
            if find_amt(s2,'"')%2==1:
                print(3)
                print("An unequal number of '\"' exists in the string")
                raise Exception("Unequal amount of quotes")
            else:
                print(4)
                foo='"'
                try:s2=s2[s.find('"')+1:]
                except IndexError:pass 
                for i in range(0,len(s2)):
                    print(s2[i])
                    if s2[i]=='"':
                        foo+='"'
                        try:s2=s2[i+1]
                        except IndexError :pass
                        break
                    else:
                        foo+=s2[i]
                l.append(foo)
                del foo
        elif s2.find('"')==0:
            if find_amt(s2,"'")%2==1:
                print("An unequal number of \"\'\" exists in the string")
                raise Exception("Unequal amount of quotes")
            else:
                foo='"'
                try:s2=s2[s.find("'")+1:]
                except IndexError:pass 
                for i in range(0,len(s2)):
                    print(s2[i])
                    if s2[i]=="'":
                        foo+="'"
                        try:s2=s2[i+1]
                        except IndexError :pass
                        break
                    else:
                        foo+=s2[i]
                l.append(foo)
                del foo
        else:
            try:
                s2=s2[1:]
            except:
                return l,len(l)
        print(l)
        
    if True:
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
if __name__=='__main__':
    print(get_args2('h"C:\\User stuff"1'))
