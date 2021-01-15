import os
import re
import socket

portip=[]
localip=None
ip=[]
liste=[]


# Returns netstat -n output as a list
def checkNet():
    return list(os.popen("netstat -n").read().split())



# Gets local ip of the computer
def getIp():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

# Gets local ip with a port number
localPortip=getIp()

# Gets local ip without port number
localip=getIp().split(".")[0] + "." + getIp().split(".")[1] + "." + getIp().split(".")[2] + "." + getIp().split(".")[3]


regex = '''^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])'''

# Checks whether given string is in ipv4 format or not by using regex
def check(Ip):
    if (re.search(regex, Ip)):
        portip.append(Ip)


# Initiliaze check function and removes foreign port number from ip address
def checklist():
    ip.clear()
    portip.clear()
    liste=checkNet()
    for e in liste:
        check(e)
    for e in portip:
        st2 = e.split(".")[0] + "." + e.split(".")[1] + "." + e.split(".")[2] + "." + e.split(".")[3]
        ip.append(st2)




#returns ip address list
def returnIP():
    checklist()
    return ip


# returns ip address with foreign port numbers
def returnIPport():
    checklist()
    return portip

#returns local ip of computer
def returnLocalIp():
    return localip

def returnLocalPortIp():
    return localPortip

