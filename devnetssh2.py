import getpass
import paramiko

host = open("devices.txt" , "r")
port = 22
username = input("Username :")
password = getpass.getpass("Password")

commands = open("commands.txt" , "rb")
commandlist = [komut.strip() for komut in commands.readlines()]

for i in host.readlines():
	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(i.strip("\n"), port, username, password)
	stdin, stdout, stderr = ssh.exec_command(commands.read())
	lines = stdout.readlines()
	print(lines)


