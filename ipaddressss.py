import ipaddress

all_subnets = {}
with open("subnets.txt", "r") as sub_file:
    for line in sub_file.readlines():
        subnet_location = line.split(",")
        location = subnet_location[0]
        subnet = ipaddress.IPv4Network(subnet_location[1].strip("\n"), True)
        all_subnets[subnet] = {'has_supernet':False}

def get_supernet(prefix):
    results = []
    f = open('subnets.txt', 'r')
    for line in f.readlines():
        subnet_location = line.split(",")
        location = subnet_location[0]
        subnet = ipaddress.IPv4Network(subnet_location[1].strip("\n"), True)
        if subnet.prefixlen == prefix:
            results.append((location, subnet))
    f.close()
    return results

def find_subnets(superloc, supernet):
    f = open('subnets.txt', 'r')
    new_file = open("newsubnets.txt", "a")
    for line in f.readlines():
        subnet_location = line.split(',')
        location = subnet_location[0]
        subnet = ipaddress.IPv4Network(subnet_location[1].strip("\n"), True)
        if not all_subnets[subnet]['has_supernet']:
            if subnet.subnet_of(supernet):
                line = line.strip("\n") + f",{superloc},{supernet}\n"
                new_file.write(line)
                all_subnets[subnet]['has_supernet'] = True
    f.close()
    new_file.close()

for prefix in range(16,33):
    for item in get_supernet(prefix):
        find_subnets(item[0], item[1])