import paramiko
import time
import getpass




locations = {
	"0": "butun_lokasyonlar.txt",
	"1":"esenyurt_lokasyonlar.txt",
	"2":"izmir_lokasyonlar"	
}


def get_interfaces(location):
	
	oneg_total = open("1G " + locations[location],"a")
	teng_total = open("10G " + locations[location],"a")
	fourg_total = open("40G " + locations[location],"a")
	hung_total = open("100G " + locations[location],"a")
	host = open(locations[location],"r")

	username = input("Username :")
	password = getpass.getpass("Password :")
	port = 22

	for item in host.readlines():
		ip = item.strip('\n').split(',')[0]
		hostname = item.strip('\n').split(',')[1]
		ssh = paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(ip, port, username, password)
		client = ssh.invoke_shell()

		client.send("ter len 0\n")
		time.sleep(1)
		client.send("show interface status\n")
		time.sleep(1)
		output = client.recv(999999)
		f = open("{}.txt".format(hostname),"w")
		f.write(output.decode())
		f.close()
		f = open("{}.txt".format(hostname),"r")

		for line in f.readlines():
			if line.startswith("Eth1/1"):
				oneg_total.write(hostname + " " +line)
			elif line.startswith("Eth1/2"):
				teng_total.write(hostname + " " +line)
			elif line.startswith("Eth1/3"):
				fourg_total.write(hostname + " " +line)
			elif line.startswith("Eth1/4"):
				hung_total.write(hostname + " " +line)
		
		f.close()
	oneg_total.close()
	teng_total.close()
	fourg_total.close()
	hung_total.close()
	print("Tüm Lokasyonların Konfigürasyonları Çekilmiştir!!!")	


print("""

Interface durumunu görmek istediğiniz lokasyonu seçiniz!

0.Hepsi
1.Esenyurt
2.Izmir


	""")

lokasyon = input("Seçiminiz :")

get_interfaces(lokasyon)