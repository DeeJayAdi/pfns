import ipaddress

def getHostsInNetowerk(ip,netmask):
    net = ipaddress.IPv4Network(ip+"/"+netmask,strict=False)
    return list(net.hosts())
