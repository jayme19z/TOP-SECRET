# Write a Python program to check for access to a specified path. Test the existence, readability, writability and executability of the specified path

import os

print('Testing:', 'hi.txt')
print('Exists:', os.access('hi.txt', os.F_OK))
print('Readable:', os.access('hi.txt', os.R_OK))
print('Writable:', os.access('hi.txt', os.W_OK))
print('Executable:', os.access('hi.txt', os.X_OK))

# I am testing my file 'hi.txt'