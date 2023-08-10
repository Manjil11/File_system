import os
from filesys import *
from unit_test import *

def is_first_run():
    flag_file_path = os.path.expanduser('~/.my_script_flag')
    if not os.path.exists(flag_file_path):
        with open(flag_file_path, 'w') as flag_file:
            flag_file.write('This is a flag file.')
        return True
    else:
        return False

def main():
    if is_first_run():
        print('Warm Welcome! Happy to see you here......')
    else:
        print('Welcome back! again mate')
    print("")
    print("")
    print("Type 'help' to see the list of available commands.")
    print("Current Working Directory:", os.getcwd())

    
    while True:
        command = input(f"\n{current_directory.name}> ")
        if not command: 
            continue
        if command == "exit":
            break
        execute_command(command)

if __name__ == "__main__":
    fs=FileSystem()
    unittest.main(exit=False)  
    main()  

