import socket

def checkPort(ip,port,show,log):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(4)
    check = s.connect_ex((str(ip),int(port)))
    s.close()

    if check == 0:
        try:
            hostname = socket.gethostbyaddr(ip)
        except:
            hostname = ip
        if show:
            print("Host: "+str(ip)+":"+str(port)+" => Open | Hostname: "+str(hostname))
        log.append({
            "host":str(ip),
            "hostname":hostname,
            "port":{
                "nr":int(port),
                "status":"Open"
            }
        })