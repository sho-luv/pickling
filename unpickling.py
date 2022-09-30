#!/usr/bin/python

import codecs
import os, sys, pickle, argparse
from base64 import b64encode, b64decode

banner = """
                       .      
 . . ,-. ,-. . ,-. . , |  ,-. 
 | | | | | | | |   |/  |  |-' 
 `-' ' ' |-' ' `-' |\  `' `-' 
         |         ' `        
         '                    
"""
parser = argparse.ArgumentParser(description='This script is used to execute pickled objects.')
parser.add_argument('pickle', action='store', metavar='pickled_object', help="Pickled objects passed here will be executed on the system this script is ran on.")

if len(sys.argv)==1:
    print( banner )
    parser.print_help()
    sys.exit(1)

options = parser.parse_args()

if options.pickle != None and "gASV" in options.pickle:
    try:
        pickle.loads(codecs.decode(options.pickle.encode(), "base64"))
    except pickle.UnpicklingError: 
        print("\nUnable to unpickle object")
        exit(1)
    print("\nUnpickled Object Successfully")
else:
    print("Not a Pickled object!")
