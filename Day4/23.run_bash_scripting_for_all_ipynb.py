import subprocess
import os

current_directory = os.getcwd()
all_files = os.listdir(current_directory+'\Day4')
print('Current directory:',current_directory+'\Day4')
#install_command = 'pip install ipynb-py-convert'
#subprocess.Popen(install_command, shell=True)

ipynb_files =[]
for filename in all_files:
    if filename.endswith('ipynb'):
        ipynb_files.append(filename)
print(ipynb_files)

for filename in ipynb_files:    
    old_file =f'{'Day4'}\\{filename}'
    new_file =f'{'Day4'}\\{filename}'.replace('ipynb', 'py') 

    command = f'ipynb-py-convert {old_file} {new_file}'
    print(command)

    subprocess.Popen(command, shell=True)