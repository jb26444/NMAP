import nmap

ipscanner = nmap.PortScanner()

ipscanner.scan("10.128.10.11", "20-443")

for host in ipscanner.all_hosts():
    print("Host : %s (%s)" % (host, ipscanner[host].hostname()))
    print("State : %s" % ipscanner[host].state())
    for protocol in ipscanner[host].all_protocols():
        print("Protocol : %s" % protocol)


        ip_port = ipscanner[host][protocol].keys()
        for port in ip_port:
            print("port : %s\tstate : %s" % (port, ipscanner[host][protocol][port]["state"]))
