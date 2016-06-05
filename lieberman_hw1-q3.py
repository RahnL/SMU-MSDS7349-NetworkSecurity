# -*- coding: utf-8 -*-
"""
Created on Fri Jun 03 15:08:34 2016
The goal of this exercise is to write a simple port scanner for 
networked systems. Using the socket library, you will create 
a script that iterates through a range of IP addresses, 
and, for each IP address, will identify the active ports available 
for that IP address. At least ports corresponding to telnet, ftp SSH, 
smtp, http, imap, and https services should be scanned and identiﬁed.
@author: rahnl
"""
from __future__ import print_function
import socket

def readSocket(ip, port):
    try:
        socket.setdefaulttimeout(1)
        s = socket.socket()
        s.connect((ip,port))
        result = s.recv(1024)
        return result
    except:
        return

def main():
    # portlist = range(1,1024)    #ports 1- 1024
    portlist = [21, 22, 25, 80, 110, 443]
    for x in range(1,255):
        ip = '172.21.101.' + str(x)
        print ('Checking: ' + ip)
        
        for port in portlist:
            print(str(port)+ '.', end="")
            banner = readSocket(ip,port)
            
            if banner:
                print ('\t--> ' + banner)
        print()      
if __name__ == '__main__':
    main()
    