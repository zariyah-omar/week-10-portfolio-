
# Name: zariyah omar 
# Username: mxbx0968@leeds.ac.uk

import sys
import os

try:
    file_name = sys.argv[1]
except IndexError:
    # No filename provided
    print("Usage: python file_line_count.py <filename.txt>", file=sys.stderr)
    sys.exit(1)

if not os.path.isfile(file_name):
    print(f"File not found: python file_line_count.py {file_name}", file=sys.stderr)
    sys.exit(1)

number_of_lines = 0
with open(file_name, 'r') as f:
    for line in f:
        if line.strip():
            number_of_lines += 1

print(f"{file_name} has {number_of_lines} lines")

# Test on the 'text_example.txt' file. The answer should be 4.
