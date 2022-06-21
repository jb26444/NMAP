from ipaddress import IPv4Network
from ipaddress import IPv4Interface

f = open("ipaddress_databasse.txt", "w")
ip = IPv4Interface("10.128.10.10/29")
net = IPv4Network(ip.network)
for addre in net:
    f.write(str(addre) + " ")
    print(addre)
f.close()

