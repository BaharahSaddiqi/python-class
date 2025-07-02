import os
import errno
try:
    file = open ("alt.txt","r")
except IOError as e:
    print(e)  
    print(e.errno)
    print(os.strerror(e.errno))
    print(errno.ENOENT)