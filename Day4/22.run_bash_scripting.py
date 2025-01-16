import subprocess
import os

current_diectory = os.getcwd()


old_file =f"{current_diectory}/2.packing_unpacking.ipynb"
new_file =f"{current_diectory}/02.packing_unpacking.py"

command = f'ipynb-py-convert { old_file} {new_file}'

subprocess.Popen(command, shell=True)