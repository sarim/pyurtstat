#!/usr/bin/env python
import socket,sys

MESSAGE="\377\377\377\377getstatus"

sock = socket.socket( socket.AF_INET,socket.SOCK_DGRAM )                    
sock.connect( (sys.argv[1], int(sys.argv[2])) )
sock.send( MESSAGE )
data, addr = sock.recvfrom( 1024 )
sock.close()

lines = data.split("\n")
urt_vars = {}
uvars =  lines[1].split("\\")
for i in range(1,len(uvars),2):
    urt_vars[uvars[i].strip()] = uvars[i+1].strip()

print 
if (len(sys.argv) > 3):
    params = sys.argv[3].split(",")
else:
    params = ['sv_hostname','mapname']
for p in params:
    print (p) + ":\t\t" + urt_vars[p]

plcount = len(lines)-3
print
print "Online Players : " + str(plcount)
print
if (plcount > 0):
    print "Ping\t\t\tKill\t\t\tName"
    print "----------------------  ----------------------  ----------------------"
    for x in range(2,plcount + 2):
        k = lines[x].split(" ")
        print k[1] + "\t\t\t" + k[0] + "\t\t\t" + k[2][1:-1]
    