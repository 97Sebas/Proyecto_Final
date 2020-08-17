import paramiko
import os

host = "192.168.1.11"

port = 22

username = "root"

password = "1234"


command = "python3 FaceD.py"


ssh = paramiko.SSHClient()

ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

ssh.connect(host, port, username, password)


stdin, stdout, stderr = ssh.exec_command(command)

lines = stdout.readlines()

print(lines)
ssh.close()