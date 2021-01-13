import paramiko
import time
import getpass

def get_ssh_vlan():

	host = ip
	username = "admin"
	password = "admin"
	port = 22

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port, username, password)
	client = ssh.invoke_shell()
	client.send("Term len 0\n")
	client.send("show vlan brief\n")
	time.sleep(1)
	output = client.recv(999999)
	output = output.decode().split('\r\n')
	tmp = []
	for item in output:
		if 'active' in item:
			tmp.append(item + "\n")
	vlan.writelines(tmp)
	vlan.close()

def get_ssh_interface():
	host = ip
	username = "admin"
	password = "admin"
	port = 22

	ssh = paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	ssh.connect(host, port, username, password)
	client = ssh.invoke_shell()
	client.send("Term len 0\n")
	client.send("show interface status | ex connected\n")
	time.sleep(1)
	output = client.recv(999999)
	inter.write(output.decode())
	inter.close()

def get_vlan(vlan_type):
	if loc == "1":
		vlan = open("Esenyurt Vlan List.txt","r")
	elif loc == "2":
		vlan = open("Tuzla Vlan List.txt","r")
	elif loc == "3":
		vlan = open("Gaziemir Vlan List.txt","r")
	elif loc == "4":
		vlan = open("Pursaklar Vlan List.txt","r")

	vlanlist = [vlanx.split()[0] for vlanx in vlan.readlines()]
	vlan.close()

	if vlan_type == '1':
		for i in range(101, 201):
			if str(i) not in vlanlist:
				return print("\nRezerve edlien ILO vlan'ı :" + " " +  str(i))
	elif vlan_type == '2':
		for i in range(201,301):
			if str(i) not in vlanlist:
				return print("\nRezerve edlien MANAGEMENT vlan'ı :" + " " +  str(i))
	elif vlan_type == '3':
		for i in range(301,401):
			if str(i) not in vlanlist:
				return print("\nRezerve edlien BACKUP vlan'ı :" + " " +  str(i))
	elif vlan_type == '4':
		for i in range(401,501):
			if str(i) not in vlanlist:
				return print("\nRezerve edlien DMZ vlan'ı :" + " " +  str(i))

def get_interface(interface_type):
	if loc == "1":
		inter = open ("Esenyurt Interface List.txt","r")
		loca = "DC90ESY01"
	elif loc == "2":
		inter = open ("Tuzla Interface List.txt","r")
		loca = "DC90TZL01"
	elif loc == "3":
		inter = open ("Gaziemir Interface List.txt","r")
		loca = "DC90GZM01"
	elif loc == "4":
		inter = open ("Pursaklar Interface List.txt","r")
		loca = "DC90PSK01"
	while True:
		for item in inter.readlines():
			if interface_type == "1" and item.startswith("Eth1/1"):
				item = item.split()
				print("\nRezerve edilen switch: " + loca) 
				return print("\nRezerve edilen port : " + item[0] + "\n")
				inter.close()
				break
			elif interface_type == "2" and item.startswith("Eth1/2"):
				item = item.split()
				print("\nRezerve edilen switch: " + loca) 
				return print("\nRezerve edilen port : " + item[0] + "\n")
				inter.close()
				break
			elif interface_type == "3" and item.startswith("Eth1/3"):
				item = item.split()
				print("\nRezerve edilen switch: " + loca) 
				return print("\nRezerve edilen port : " + item[0] + "\n")
				inter.close()
				break
		break

loc = input("""
****** LOKASYONLAR ******

1.ESENYURT
2.TUZLA
3.IZMIR
4.PURSAKLAR

Seçiminiz :""")

vlan_type = input("""
***** VLANLAR *****

1.ILO        - Vlan id 101-200
2.MANAGEMENT - Vlan id 201-300
3.BACKUP     - Vlan id 301-400
4.DMZ        - Vlan id 401-500


Seçiminiz :""")

interface_type = input("""
****** INTERFACE TIPI ******

1.1G COPPER
2.10G COPPER
3.10G FIBER

Seçiminiz :""")	

if loc == "1":
	vlan = open("Esenyurt Vlan List.txt","w")
	inter = open ("Esenyurt Interface List.txt","w")
	ip = "192.168.1.101"
elif loc == "2":
	vlan = open("Tuzla Vlan List.txt","w")
	inter = open ("Tuzla Interface List.txt","w")
	ip = "192.168.1.102"
elif loc == "3":
	vlan = open("Gaziemir Vlan List.txt","w")
	inter = open ("Gaziemir Interface List.txt","w")
	ip = "192.168.1.201"
elif loc == "4":
	vlan = open("Pursaklar Vlan List.txt","w")
	inter = open ("Pursaklar Interface List.txt","w")
	ip = "192.168.1.202"

get_ssh_vlan()
get_ssh_interface()
get_vlan(vlan_type)
get_interface(interface_type)


vlan.close()
inter.close()
