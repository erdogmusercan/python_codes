
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

with open("netmiko1_config_file.txt") as f:
	lines = f.read().splitlines()
print(lines)


for devices in all_devices:
	net_connect = ConnectHandler(**devices)
	output = net_connect.send_config_set(lines)
print("All configuration in the netmiko1_config_file.txt are completed!")
