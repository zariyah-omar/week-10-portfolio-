
# Name:zariyah omar 
# Username:  mxbx0968@leeds.ac.uk

# Lists contents of a zip archive
# usage: python ziplist.py <zipfile>
# eg. python ziplist.py testdir/test.zip
# You must use the error messages precisely as defined below.

# Hint: look at the documentation for the "zipfile" module

import sys
import os
import zipfile
#from zipfile import ...   # tools in this module can be used

# filename is a command line argument 
file_name = ""
if len(sys.argv) != 2:
    print("Usage: python ziplist.py <filename.zip>", file=sys.stderr)
    sys.exit(1)
file_name = sys.argv[1]
if not os.path.isfile(file_name):
    print(f"File not found: python ziplist.py {file_name}", file=sys.stderr)
    sys.exit(1)
try:
    with zipfile.ZipFile(file_name, 'r') as zip_ref:
        # List the contents of the zip file
        for file in zip_ref.namelist():
            print(file)
except zipfile.BadZipFile:
    print(f"Bad zip file: python ziplist.py {file_name}", file=sys.stderr)
    sys.exit(1)
# Error message: "Usage: python ziplist.py <filename.zip>"

# Error message: "File not found: python ziplist.py {file_name}"

# Error message: "Bad zip file: python ziplist.py {file_name}"
# Hint: There is an exception for this defined in the zipfile module

# Use zipfile methods to list the contents of the zip file.
# Test your script on the zip_example.zip file. The response should be:
# README.md
# cmd_line.py
# find_file.py
# password.py
# rockpaperscissors.py
