from ipaddress import IPv4Network

f = open("ipaddress_databasse.txt", "w")
net = IPv4Network("10.128.10.8/29")
for addre in net:
    f.write(str(addre))
    print(addre)
f.close()

