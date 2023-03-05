#!/usr/bin/bash python3

# Above makes this file executavble from the command line, making this file useable by an automated task
# Imports the required libraries 
import sys
import logging
import paramiko
from datetime import datetime as dt

# Defines current time and date.
now = dt.now()
# Logging for debuggin, and quality control
logging.basicConfig(filename='sftp.log', level=logging.DEBUG)


### Function Variables: Change variables here, pre loaded into function below 
HOST_NAME = '192.168.1.244' # --->  Dell PowerEdge R620 on my local network
PORT = 22   
USERNAME = ''
PASSWORD = ''
METHOD = 'GET'  
FILEPATH = 'test.txt'
LOCALPATH = '/home/jesse/Desktop'

# Paramiko Library ---> https://docs.paramiko.org/en/stable/api/sftp.html
# Function to Established connection abnd retrieve files on remote server following STFP protocal
def SFTP(host_name, port, username, password, filepath, localpath, command=None, method="GET"):
    # Log initial function call
    logging.info(f'[{now}]: SFTP INITIALIZED!!!')
    # Try/excpet code block
    try:
        # Establishes SSH Stream to a Socket or Socket like Object
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(host_name, port, username, password)
            logging.info('SSHClient: Success')

            sftp = client.open_sftp()

            if method == 'GET':
                sftp.get(filepath, localpath)
                logging.info(f'[{now}]: client SFTP download success')
                sftp.close()
            else:
                sftp.put(localpath, filepath)
                logging.info(f"[{now}]: client SFTP upload success")
                sftp.close

            _, stdout, stderr = client.exec_command(command)
            output = stdout.readlines() + stderr.readlines()
            if output:
                logging.info(f"[{now}]")
                for line in output:
                    logging.info(line.strip())

        except Exception as e:
            logging.error(f'SSHClient ERROR: {e}')

        # If no connection made
        else:
            # Loggin to sftp.log file for debugging
            logging.debug(f'[{now}]: Connection not open...')
    # Catch an ERROR     
    except Exception as e:
        # Catch ERROR and log auto log to the sftp.log file for debugging
        logging.error(f'[{now}] Failure in SFTP function: {e}.')

# Runs the script
if __name__ == '__main__':
    # Calls the SFTP Function and passes in the arguments defined above (per convention -- ALL CAPS denote global variables)
    SFTP(HOST_NAME, PORT, USERNAME, PASSWORD, FILEPATH, LOCALPATH)
    # If script completes execution, logs success meesage to sftp.log file 
    logging.info(f'[{now}]: SFTP COMPLETE')
    # Exit Shell Script
    sys.exit()
