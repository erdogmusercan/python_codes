
from netmiko import ConnectHandler

nx_os1 = {
	"device_type":"cisco_nxos",
	"ip":"192.168.1.101",
	"username":"admin",
	"password":"admin",
}

nx_os2 = {
	"device_type":"cisco_nxos",
	"ip":"192.168.1.102",
	"username":"admin",
	"password":"admin",
}

all_devices = [nx_os1,nx_os2]

for devices in all_devices:


	net_connect = ConnectHandler(**devices)
	output = net_connect.send_command("show ip int brie vrf all")

	print(output)

	

#		if str(devices) == "nx_os1":
#
#			config_commands = ["int loop 0" , "ip address 1.1.1.1 255.255.255.255"]
#			output = net_connect.send_config_set(config_commands)
#			print(output)
#		elif str(devices) == "nx_os2":
#
#			config_commands = ["int loop 0" , "ip address 2.2.2.2 255.255.255.255"]
#			output = net_connect.send_config_set(config_commands)
#			print(output)
	

	for n in range (100,121):
		print("Creating Vlan" + str(n))
		config_commands = ["vlan " + str(n), "name Python_Vlan" + str(n)]
		output = net_connect.send_config_set(config_commands)
		print(output)

print("Configurations are completed!!")
