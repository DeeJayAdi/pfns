import socket
import ipaddress
from datetime import datetime
from threading import Thread
from lib.saveLog import *
from lib.checkPort import *
from lib.getHostsInNetwork import *
from art import tprint
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-b','--broadcast',help="Specifie the broadcast ip",required=True)
parser.add_argument('-n','--netmask',help="Specifie the netmask",required=True)
parser.add_argument('-p','--port',help="Specifie port number",required=True)
parser.add_argument('-sl','--savelog',action="store_true",help="Save logs to file",default=False)
parser.add_argument('-s','--show',action="store_true",help="Show logs",default=False)
args = parser.parse_args()

broadcast = args.broadcast
netmask = args.netmask
port = args.port

log=[]

tprint("PFNS")

print("PFNS - Python Fast Network Scanner\n")

print("Started scanning...")
print("--------------------------------------------")

startTime = datetime.now()

hosts = getHostsInNetowerk(broadcast, netmask)

threads = []

for ip in hosts:
    threads.append(Thread(target=checkPort,args=(str(ip),port,args.show,log)))
for host in threads:
    host.start()
for host in threads:
    host.join()

print("--------------------------------------------")
endTime = datetime.now()

if args.savelog:
    saveLog(log)

print("Scanning ended!")
print("Duration: "+str(endTime-startTime))
print("--------------------------------------------")
