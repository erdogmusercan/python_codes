import getpass
import telnetlib

HOST = "192.168.1.101"
user = input("Username: ")
password = getpass.getpass()

tn = telnetlib.Telnet(HOST)

tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
	tn.read_until(b"Password: ")
    	tn.write(password.encode('ascii') + b"\n")

tn.write(b"conf t\n")
tn.write(b"vlan 1972\n")
tn.write(b"name Test\n")
tn.write(b"exit\n")
tn.write(b"end\n")
tn.write(b"copy runn star\n")

print(tn.read_all().decode('ascii'))
