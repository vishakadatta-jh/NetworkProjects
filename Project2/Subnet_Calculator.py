        #!/usr/bin/env python
        # coding: utf-8

        # In[1]:


import sys
import random

def subnet_calculator():       # In[84]:
    try:
        while True:
            ip_addr = input('Enter a valid IP address: ')
            octet = ip_addr.split('.')
            if len(octet) == 4 and 1 <= int(octet[0]) <= 223             and (int(octet[0]) != 169 or int(octet[1]) != 254)             and int(octet[0] != 127) and 1 <= int(octet[1]) <= 255             and 1 <= int(octet[2]) <= 255 and 1 <= int(octet[3]) <= 255:
                break
            else:
                print ("\n*****Invalid or Reserved address !! Try again*****\n")
                continue

        masks =[255,254,252,248,240,224,192,128,0]
        while True:
            subnet_addr = input('Enter a subnet mask: ')
            subnet_octet = subnet_addr.split('.')
            if len(subnet_octet) == 4 and int(subnet_octet[0]) == 255 and (int(subnet_octet[1]) in masks) and (int(subnet_octet[2]) in masks) and (int(subnet_octet[3]) in masks) and                      int(subnet_octet[0])>=int(subnet_octet[1])>=int(subnet_octet[2])>=int(subnet_octet[3]) :
                break
            else:
                print ("\n*****Invalid SUBNET Try again !!*****\n")
                continue
        #print(subnet_octet)


        # In[85]:


        #Converting subnet to binary
        masks_octet_binary =[]

        for i in subnet_octet:
            binary_octet = bin(int(i)).lstrip('0b') #default output is always '0b1001' so we remove the '0b'
            masks_octet_binary.append(binary_octet.zfill(8)) #always we need to have 8bits '00000001' instead of '01'
            
        binary_mask ="".join(masks_octet_binary) #this join would given an output like "11111111111111111111111111000000"

        #Converting ip address to binary
        ip_octet_binary =[]

        for i in octet:
            binary_octet = bin(int(i)).lstrip('0b') #default output is always '0b1001' so we remove the '0b'
            ip_octet_binary.append(binary_octet.zfill(8)) #always we need to have 8bits '00000001' instead of '01'
            
        binary_ip ="".join(ip_octet_binary) #this join would given an output like "11111111111111111111111111000000"

        zeros_count = binary_mask.count('0')
        ones_count = 32 - zeros_count
        hosts_count = (2 ** zeros_count - 2) #no of hosts formula 

        #now finding the wildcard mask
        #slash...Subnet........Wildcard Mask
        #/32	255.255.255.255	0.0.0.0
        #/31	255.255.255.254	0.0.0.1
        #/30	255.255.255.252	0.0.0.3
        #/19	255.255.224.0	0.0.31.255
        #/18	255.255.192.0	0.0.63.255
        #/17	255.255.128.0	0.0.127.255
        wildcard_octet = []

        for i in subnet_octet:
            wild_mask = 255 - int(i)
            wildcard_octet.append(str(wild_mask)) #['0','0','0','255']
            #print(wildcard_octet)
        wildcard_mask = '.'.join(wildcard_octet)


        # In[97]:


        # Extracting the Network and Broadcast address from the IP address
        # print(binary_ip)
        # binary_ip = 0B00000001000000010000000100000001
        # type(binary_ip)
        network_address_binary = binary_ip[:ones_count] + '0' * zeros_count
        #print(network_address_binary)

        broadcast_address_binary = binary_ip[:ones_count] + '1' * zeros_count
        #print(broadcast_address_binary)

        net_octet = []

        for i in range(0,32,8):
            net_octets = network_address_binary[i : i+8]
            net_octet.append(net_octets)
        # print(net_octet)

        net_ip = []

        for i in net_octet:
            net_ip.append(str(int(i,2)))
        # print(net_ip)
            
        network_address = ".".join(net_ip)
        # print(network_address)    
            
        bc_octet = []

        for i in range(0,32,8):
            bc_octets = broadcast_address_binary[i : i+8]
            bc_octet.append(bc_octets)
        #print(bc_octet)

        bc_ip = []

        for i in bc_octet:
            bc_ip.append(str(int(i,2)))
        #print(bc_ip)
            
        broadcast_address = ".".join(bc_ip)
        #print(broadcast_address)    
            


        # In[98]:


        print("\n")
        print("Network Address is: %s" %network_address)
        print("Broadcast Address is: %s" %broadcast_address)
        print("Number of Hosts is: %d"%hosts_count)
        print("Wildcard Mask is: %s"%wildcard_mask)
        print("Mask Bits: %s"%ones_count)
        print("\n")
        
        #Creating a random IP address generator in the subnet
        while True:
            request = input("Do you want a random IP address from subnet  (Y/N): ")
            
            if request == 'Y' or request =='y':
                random_ip = []
                
                for i_b,bc_octet in enumerate(broadcast_address):
                    for i_n,net_octet in enumerate(network_address):
                        if i_n == i_b:
                            if net_octet == bc_octet:
                                random_ip.append(bc_octet)
                            else:
                                random_ip.append(str(random.randint(int(net_octet),int(bc_octet))))
                random_address = "".join(random_ip)
                #print(random_address)
                #print(random_ip)
                print("Random IP in the given subnet is: %s" %random_address)
                print("\n")
                continue
            else:
                print("OK BYE!!!\n")
                break
                                

    except KeyboardInterrupt:
        print('\nUser KeyboardInterrupt captured.........Program exited\n')
        sys.exit()

subnet_calculator()