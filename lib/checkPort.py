import socket

def checkPort(ip,port,show,log):
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    s.settimeout(4)
    check = s.connect_ex((str(ip),int(port)))
    s.close()

    if check == 0:
        if show:
            print("Host: "+str(ip)+":"+str(port)+" => Open")
        log.append({
            "host":str(ip),
            "port":{
                "nr":int(port),
                "status":"Open"
            }
        })