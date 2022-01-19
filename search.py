import sys, re
from os import listdir, path

tofound = input('Enter string to found:\t')
x = input('Enter to be found in(directory):\t')

def getdir(x):
    br = False
    a = listdir(x)
    for i in a:
        if(br):
            break
        else:
            if path.isdir(x + '\\'+ i):
                getdir(x + '\\'+ i)
            else:
                if((x +'\\'+i).split('.')[-1] != 'rar'):
                    with open(x +'\\'+i, 'r', encoding="utf-8") as f1:
                        s = f1.read()
                        # re.search() returns a Match object if there is a match anywhere in the string
                        if re.search( tofound, s ):
                            print("Found '{0}' in this '{1}' file. " .format(tofound, x +'\\'+i))
                            br = True


getdir(x)