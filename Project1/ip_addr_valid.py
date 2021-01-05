# Vishakdatta JH #Project_1
import sys

# length shd be 4 ,convert to int  ,1<add<223,127,[0]169 or [1]254,other 3 octets betwee 0--255

def ip_addr_valid(list):
    for i in list:
        i = i.rstrip('\n')
        octet = i.split('.')
        
        if((len(octet) == 4) and (1 <= int(octet[0]) <= 223) and ((int(octet[0])!= 169) or (int(octet[1]) != 254)) and (int(octet[0] != 127)) and 1<=int(octet[1])<=255 and 1<=int(octet[2])<=255 and 1<=int(octet[3])<=255):
            continue
        else:
            print("Invalid or Reserved address !!")
            sys.exit()
            