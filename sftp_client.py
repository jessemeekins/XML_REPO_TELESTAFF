#!/bin/bash

import sys
import paramiko
import logging
from datetime import datetime as dt

now = dt.now()
logging.basicConfig('sftp.log', level=logging.DEBUG)


HOST_NAME = 'memphistn-wfts-xfer.kronos/PROD/files'
PORT = 22
USERNAME = ''
PASSWORD = ''
METHOD = 'GET'
FILEPATCH = '/var/bin/bash'
LOCALPATH = '/Documents/XML_FILES'


def SFTP(host_name, port, username, password, filepath, localpath, method="GET"):

    try:    

        try:
            transport = paramiko.Transport((host_name,port))
        except:
            e = sys.exc_info()[0]
            logging.error(f'[paramiko.Transport]: {e}.')
        
        try:
            transport.connect(None,username,password)
        except:
            e = sys.exc_info()[0]
            logging.error(f'[transport.connect]: {e}.')

        try:
            sftp = paramiko.SFTPClient.from_transport(transport)
        except:
            e = sys.exc_info()[0]
            logging.error(f'[paramiko.SFTPClient.from_transport]: {e}.')
        
        if method == 'GET':
            try:
                sftp.get(filepath,localpath)
            except:
                e = sys.exc_info()[0]
                logging.error(f'[sftp.get]: {e}.')
        else:
            try:
                sftp.put(localpath,filepath)
            except:
                e = sys.exc_info()[0]
                logging.error(f'[sftp.put]: {e}.')

        try:
            if sftp: 
                sftp.close()
            if transport: 
                transport.close()
        except:
            e = sys.exc_info()[0]
            logging.error(f'[CONNECTION CLOSED]: {e}.')
            

    except Exception as e:
        logging.error(f'[{now}] Failure in main function: {e}.')


if __name__ == '__main__':
    SFTP(HOST_NAME, PORT, USERNAME, PASSWORD, FILEPATCH, LOCALPATH)