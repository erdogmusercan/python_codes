import getpass
import telnetlib

HOST = ["192.168.1.101","192.168.1.102"]
user = input("Enter your usernmame: ")
password = getpass.getpass()

for i in HOST:

	tn = telnetlib.Telnet(i)

	tn.read_until(b"login:")
	tn.write(user.encode('ascii') + b"\n")
	if password:
    		tn.read_until(b"Password: ")
    		tn.write(password.encode('ascii') + b"\n")

	tn.write(b"conf t\n")
	tn.write(b"vlan 1972\n")
	tn.write(b"name Finco\n")
	tn.write(b"end\n")
	tn.write(b"copy runn start\n")
	tn.write(b"exit\n")
	tn.write(b"\n")

	print(tn.read_all().decode('ascii'))


