# Write a Python program to list only directories, files and all directories, files in a specified path.
import os

print('current directory')
current_dir = os.listdir()
print(current_dir)

'''
My output:
current directory
['bf_1.py', 'bf_2.py', 'bf_3.py', 'bf_4.py', 'bf_5.py', 'dir_1.py', 'dir_2.py', 
'dir_3.py', 'dir_4.py', 'dir_5.py', 'dir_6.py', 'dir_7.py', 'dir_8.py']
'''

print('specified directory')
print(os.listdir('C:/Users/kozha/OneDrive/Рабочий стол/edu'))

'''
My output:
specified directory
['1st year of uni', 'books', 'Database Design and Business Intelligence Implementation', 
'Discrete Structures', 'EQ course', 'Exchange program', 'Introduction to Algorithms', 
'Introduction to Optimization', 'Korean Language', 'Programming Principles II', 'Russian Language', 
'РУП - IT Management 1208.xlsx']
'''
