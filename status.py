import paramiko
import getpass
import time

host = open("host.txt" , "r")

username = ""
p = ""

for item in host.readlines():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(item.strip("\n"), username=username, password=p , port =22)

    channel = ssh.invoke_shell()
    time.sleep(2)
    channel.send("\nter len 0\n")
    time.sleep(1)
    channel.send("sh interface status | ex connected | ex Eth1/ | ex Eth2/ | ex Eth3/ | ex Eth4/ | ex Po | ex Vlan | count\n")
    time.sleep(5)
    channel.send("sh interface status | ex connected | ex Eth1/ | ex Eth2/ | ex Eth3/ | ex Eth4/ | ex Po | ex Vlan\n")
    time.sleep(5)
    output = channel.recv(655350)

    f = open("{}.txt.".format(item.split()), "w")
    f.write(output.decode())
    f.close()
    print("{} Konfigurasyon çekildi.".format(item))
