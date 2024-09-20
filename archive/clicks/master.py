####################################################################################
## This script is the workflow of the project


from platform import python_version
import sys
import os
import time
from datetime import datetime

start_time = time.time()


# script master to run ALL the steps of the project. 
def main():

    # checking the python version:
    if sys.version_info<(3,6,0):
        py_version = python_version()
        print(f'The python version installed in your computer: {py_version}')
        sys.stderr.write("You need python 3.6 or later to run this script\n")
        sys.exit()
        
    else:
        py_version = python_version()
        print(f'python version: {py_version}')
        print('Successfully, go ahead to run the script.')

    # Get start time 
    start_time = time.time()

    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(">>> date: ", dt_string)
    
    # step 1
    os.system('python3.8 clickon.py') # > logs/info-preprocess.dat
    

    time_exec_min = round( (time.time() - start_time)/60, 4)
    
    print(f'time of execution (total pipeline): {time_exec_min} minutes')
    # datetime object containing current date and time
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    print(">>> date: ", dt_string)
    print('Done! :)')


if __name__ == "__main__":

    while True:
        main()
        
