#operating system
import os
from pprint import pprint

current_directory = os.getcwd()
print("The current directory is:",current_directory)

all_files = (os.listdir('C:/Users/training/Desktop/PytonMichelin/Day 1/Day2')) #current directory or any directory to be written
print(type(all_files))

extensions = ['py','ipynb']

filtered_files = []
for filename in all_files:
    if filename.endswith(extensions[0]) or filename.endswith(extensions[1]):
        filtered_files.append(filename)

filtered_files = sorted(filtered_files)
print(filtered_files)

#test file renamed
#os.rename('C:/Users/training/Desktop/Github-Ildiko/__test.py','C:/Users/training/Desktop/Github-Ildiko/__test_renamed.py' )
files_to_remane = []
for filename in filtered_files:
    if filename[1] == '.' and filename[0].isnumeric():
        files_to_remane.append(filename)
print(files_to_remane)

for filename in files_to_remane:

    os.rename('C:/Users/training/Desktop/PytonMichelin/Day 1/Day2'+'/'+filename, 'C:/Users/training/Desktop/PytonMichelin/Day 1/Day2'+'/0'+filename)