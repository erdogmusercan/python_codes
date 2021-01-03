import paramiko
import getpass
import time

host = open("devices.txt", "r")
port = 22
username = input("Username :")
password = getpass.getpass("Password")

commands = open("commands.txt", "r")
commandlist = [komut for komut in commands.readlines()]

for i in host.readlines():

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(i.strip("\n"), port, username, password)
    stdin , stdout , stderr = ssh.exec_command(commandlist)
    client = ssh.invoke_shell()

    for command in commandlist:

   		file = open("{}.txt".format(i), "a")
   		client.send(command)
   		lines = client.recv(2048)
   		file.write(SSHClient.stdout.readlines())
   		file.close()


