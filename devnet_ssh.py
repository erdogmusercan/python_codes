import getpass
import paramiko
import time

host = open("devices.txt" , "r")
port = 22
username = input("Username :")
password = getpass.getpass("Password")

commands = open("commands.txt" , "r")
commandlist = [komut for komut in commands.readlines()]
for i in host.readlines():


		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(i.strip("\n"), port, username, password)
		client = ssh.invoke_shell()
		file = open("{}.txt".format(i) , "w")

		for command in commandlist:
			
			client.send(command)
			time.sleep(0.4)
			lines = client.recv(4096)
			print(lines)
			file.write(lines.decode())
		file.close()


