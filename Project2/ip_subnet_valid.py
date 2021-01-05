#!/usr/bin/env python
# coding: utf-8

# length shd be 4 ,convert to int  ,1<add<223,127,[0]169 or [1]254,other 3 octets betwee 0--255
def ip_addr_valid():
    while True:
        ip_addr = input('Enter a valid IP address: ')
        octet = ip_addr.split('.')
        if len(octet) == 4 and 1 <= int(octet[0]) <= 223             and (int(octet[0]) != 169 or int(octet[1]) != 254)             and int(octet[0] != 127) and 1 <= int(octet[1]) <= 255             and 1 <= int(octet[2]) <= 255 and 1 <= int(octet[3]) <= 255:
            break
        else:
            print ("\n*****Invalid or Reserved address !! Try again*****\n")
            continue

masks =[255,254,252,248,240,224,192,128,0]
def ip_subnet_valid():
    while True:
        global subnet_addr
        subnet_addr= input('Enter a subnet mask: ')
        global subnet_octet 
        subnet_octet = subnet_addr.split('.')
        if len(subnet_octet) == 4 and int(subnet_octet[0]) == 255 and (int(subnet_octet[1]) in masks) and (int(subnet_octet[2]) in masks) and (int(subnet_octet[3]) in masks) and                      int(subnet_octet[0])>=int(subnet_subnet_octet[1])>=int(subnet_octet[2])>=int(subnet_octet[3]) :
            break
        else:
            print ("\n*****Invalid SUBNET Try again !!*****\n")
            continue
# ip_addr_valid()
#ip_subnet_valid()