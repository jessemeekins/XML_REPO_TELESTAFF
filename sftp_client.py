#!/usr/bin/bash/python

# Above makes this file executavble from the command line, making this file useable by an automated task
# Imports the required libraries 
import sys
import logging
import paramiko
from datetime import datetime as dt

# Defines current time and date.
now = dt.now()
# Logging for debuggin, and quality control
logging.basicConfig('sftp.log', level=logging.DEBUG)


### Function Variables: Change variables here, pre loaded into function below 
HOST_NAME = '/some/server/on/a/network'
PORT = 22
USERNAME = ''
PASSWORD = ''
METHOD = 'GET'
FILEPATCH = '/file/path/to/retrieve'
LOCALPATH = '/file/path/to/save'

# Paramiko Library ---> https://docs.paramiko.org/en/stable/api/sftp.html
# Function to Established connection abnd retrieve files on remote server following STFP protocal
def SFTP(host_name, port, username, password, filepath, localpath, method="GET"):
    # Log initial function call
    logging.info(f'[{now}]: SFTP INITIALIZED!!!')
    # Try/excpet code block
    try:
        # Establishes SSH Stream to a Socket or Socket like Object
        transport = paramiko.Transport((host_name,port))
        # Immediatly sends back True or False when attempting to connect
        transport.connect(None,username,password)

        # Checks if Transport connection is True
        if paramiko.Transport.is_active():
            # Defines the SFTP object
            sftp = paramiko.SFTPClient.from_transport(transport)
            # Checking if function wants to get or recieve Files: Default to GET functionality
            if method == 'GET':
                # First arg is the location of the file you want to move
                # Second arg is the save location of the file
                sftp.get(filepath,localpath)
            else:
                # Locates the locates the local file you wish to send,
                # Then the location you wish to send it
                sftp.put(localpath,filepath)

            # If either sftp or tranport was successfull, close connection. 
            if sftp: 
                sftp.close()
            if transport: 
                transport.close()
        # If no connection made
        else:
            # Loggin to sftp.log file for debugging
            logging.debug(f'[{now}]: Connection not open...')
    # Catch an ERROR     
    except Exception as e:
        # Catch ERROR and log auto log to the sftp.log file for debugging
        logging.error(f'[{now}] Failure in main function: {e}.')

# Runs the script
if __name__ == '__main__':
    # Calls the SFTP Function and passes in the arguments defined above (per convention -- ALL CAPS denote global variables)
    SFTP(HOST_NAME, PORT, USERNAME, PASSWORD, FILEPATCH, LOCALPATH)
    # If script completes execution, logs success meesage to sftp.log file 
    logging.info(f'[{now}]: SFTP SUCCESS!!!')
    # Exit Shell Script
    sys.exit()
