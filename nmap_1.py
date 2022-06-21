import nmap
from ipaddress import IPv4Address
from ipaddress import IPv4Network


address_list = list()
net = IPv4Network("10.128.10.8/29")
for addre in net:
    #address_list.append(addre)
    print(addre)


ipscanner = nmap.PortScanner()

ipscanner.scan("185.33.156.0/24", "1-1024",)

for host in ipscanner.all_hosts():
    print("Host : %s (%s)" % (host, ipscanner[host].hostname()))
    print("State : %s" % ipscanner[host].state())
    for protocol in ipscanner[host].all_protocols():
        print("Protocol : %s" % protocol)


        ip_port = ipscanner[host][protocol].keys()
        for port in ip_port:
            print("port : %s\tstate : %s" % (port, ipscanner[host][protocol][port]["state"]))
