# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 15:08:34 2016
@author: rahnl

The goal of this exercise is to write a simple port scanner for 
networked systems. Using the socket library, you will create 
a script that iterates through a range of IP addresses, 
and, for each IP address, will identify the active ports available 
for that IP address. At least ports corresponding to telnet, ftp SSH, 
smtp, http, imap, and https services should be scanned and identiﬁed.

common port list from
  http://www.yougetsignal.com/tools/open-ports/ and
  http://mobinnet.ir/uploaded/common_ports.pdf
"""
from __future__ import print_function
import socket

def readSocket(ip, port):
    try:
        socket.setdefaulttimeout(2)
        s = socket.socket()
        s.connect((ip,port))
        result = s.recv(1024)
        return result
    except:
        return

def main():
    # portlist = range(1,1024)    #ports 1- 1024
    portlist = [21, 22, 23, 25, 53, 80, 110, 115, 135, 139, 143, 194, 443,
                445, 1433, 3306, 3389, 5632, 5900, 6112,
                4444, 5554, 6881,  1080, 8866, 9898, 9988, 12345, 27374,
                28960, 31337, ]
    for x in range(1,50):
        ip = '192.168.2.' + str(x)
        print ('Checking: ' + ip)
        
        for port in portlist:
            print(str(port)+ '.', end="")
            banner = readSocket(ip,port)
            
            if banner:
                print ('\t--> ' + banner)
                
        print()      
if __name__ == '__main__':
    main()
    