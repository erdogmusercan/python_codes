
from netmiko import ConnectHandler

nx_os = {
	"device_type":"cisco_nxos",
	"ip":"192.168.1.101",
	"username":"admin",
	"password":"admin",
}

net_connect = ConnectHandler(**nx_os)
output = net_connect.send_command("show ip int brie vrf all")
print(output)

config_commands = ["int loop 0" , "ip address 1.1.1.1 255.255.255.255"]
output = net_connect.send_config_set(config_commands)
print(output)

for n in range (100,121):
	print("Creating Vlan" + str(n))
	config_commands = ["vlan " + str(n), "name Python_Vlan" + str(n)]
	output = net_connect.send_config_set(config_commands)
	print(output)
