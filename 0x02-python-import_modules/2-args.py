#!/usr/bin/python3
import sys
if len(sys.argv) - 1 == 1:
    print("{} argument:\n".format(len(sys.argv) - 1))
elif len(sys.argv) -1 == 0:
    print("{} arguments.".format(len(sys.argv) - 1))
else:
     print("{} arguments:".format(len(sys.argv) - 1))
     for i in range(len(sys.argv) - 1):
         print("{}: {}".format(i+1, (sys.argv[i+1])))
